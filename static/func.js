// Get DOM elements
const chatbox = document.getElementById('chatbox');
const msgInput = document.getElementById('messageInput');
const sendBtn = document.getElementById('sendButton');
const delBtn = document.getElementById('deleteAllBtn');
const loadingIndicator = document.getElementById('loading');
const errorIndicator = document.getElementById('error');

// Listen for input changes in the message input field
msgInput.addEventListener('input', () => {
  if (msgInput.value.trim() === '') {
    sendBtn.classList.add('disabled');
    sendBtn.disabled = true;
  } else {
    sendBtn.classList.remove('disabled');
    sendBtn.disabled = false;
  }
});

// Scroll to the bottom of the chatbox
function scrollToBottom() {
  chatbox.scrollTop = chatbox.scrollHeight;
}

// Send a message via a button click
const sendButtonMessage = (btnmessage, role) => {
  const message = btnmessage;
  loadingIndicator.style.display = 'flex';
  msgInput.disabled = true;
  sendBtn.classList.add('disabled');
  errorIndicator.style.display = 'none';

  // Send a message to the server
  fetch('http://localhost:5000/api/send_message', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ message, role })
  })
    .then(response => response.json())
    .then(data => {
      console.log('Message sent', data);
      getAndSortMessages();
      delBtn.style.display = "block";
      errorIndicator.style.display = 'none';
      loadingIndicator.style.display = 'none';
      msgInput.disabled = false;
      sendBtn.classList.remove('disabled');
      msgInput.focus();
    })
    .catch(error => {
      // Handle errors here
      console.error('Error:', error);
      getAndSortMessages();
      delBtn.style.display = "block";
      errorIndicator.style.display = 'flex';
      loadingIndicator.style.display = 'none';
      msgInput.disabled = false;
      sendBtn.classList.remove('disabled');
      msgInput.focus();
      
    });
};

// Send a message via the input field
const sendMessage = (role) => {
  const message = msgInput.value;
  tempmessage = {
    "content": message,
    "id": 696969,
    "is_user": true
  };
  showTempMessage(tempmessage);
  loadingIndicator.style.display = 'flex';
  msgInput.disabled = true
  sendBtn.classList.add('disabled');
  errorIndicator.style.display = 'none';

  // Send a message to the server
  fetch('http://localhost:5000/api/send_message', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ message, role })
  })
    .then(response => response.json())
    .then(data => {
      console.log('Message sent', data);
      msgInput.value = '';
      getAndSortMessages();
      delBtn.style.display = "block";
      errorIndicator.style.display = 'none';
      loadingIndicator.style.display = 'none';
      msgInput.disabled = false;
      sendBtn.classList.remove('disabled');
      msgInput.focus();
    })
    .catch(error => {
      // Handle errors here
      console.error('Error:', error);
      msgInput.value = '';
      getAndSortMessages();
      delBtn.style.display = "block";
      errorIndicator.style.display = 'flex';
      loadingIndicator.style.display = 'none';
      msgInput.disabled = false;
      sendBtn.classList.remove('disabled');
      msgInput.focus();
    });
};

// Send message when the send button is clicked
sendBtn.addEventListener('click', () => {
  sendMessage("user");
  msgInput.value = '';
});

// Send message when Enter key is pressed in the input field
msgInput.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') {
    sendMessage("user");
    msgInput.value = '';
  }
});

// Display temporary message and fetch and sort all messages
const showTempMessage = (tempmessage) => {
  delBtn.style.display = "block";

  // Fetch user messages
  fetch('http://localhost:5000/api/get_user_messages')
    .then(response => response.json())
    .then(data => {
      const userMessages = data.messages;

      // Fetch AI messages
      fetch('http://localhost:5000/api/get_ai_messages')
        .then(response => response.json())
        .then(data => {
          const aiMessages = data.messages;
          const allMessages = aiMessages.concat(userMessages).concat(tempmessage);
          allMessages.sort((a, b) => a.id - b.id);
          displayMessages(allMessages);
          scrollToBottom();
        });
    });
}

// Fetch and sort all messages
const getAndSortMessages = () => {
  delBtn.style.display = "block";

  // Fetch user messages
  fetch('http://localhost:5000/api/get_user_messages')
    .then(response => response.json())
    .then(data => {
      const userMessages = data.messages;

      // Fetch AI messages
      fetch('http://localhost:5000/api/get_ai_messages')
        .then(response => response.json())
        .then(data => {
          const aiMessages = data.messages;
          const allMessages = aiMessages.concat(userMessages);
          allMessages.sort((a, b) => a.id - b.id);
          if (allMessages.length === 0) {
            delBtn.style.display = "none";
          }
          displayMessages(allMessages);
          scrollToBottom();
        });
    });
}

// Display messages in the chatbox
const displayMessages = (messages) => {
  chatbox.innerHTML = '';

  messages.forEach(msg => {
    const msgDiv = document.createElement('div');
    msgDiv.textContent = msg.content;

    if (msg.is_user === true) {
      msgDiv.classList.add('user-message');
    } else {
      msgDiv.classList.add('ai-message');
    }

    // Check if the message has a button
    if (msg.button) {
      const buttonData = JSON.parse(msg.button);
      const { endpoint, function_name, args } = buttonData;

      // Create a button element
      const button = document.createElement('button');
      button.classList.add('actionbtn');
      button.textContent = buttonData.label || 'Perform Action'; // Provide a default label if not specified

      // Append the button to the message div
      msgDiv.appendChild(button);

      // Add a click event handler to call the function
      button.addEventListener('click', () => {
        buttonmessage = "The function " + function_name + " has been executed successfully. Inform the user about it."
        sendButtonMessage(buttonmessage, "system")
        button.className = "actionbtndone"
        button.textContent = buttonData.label || 'Executing Action...';
      });
    }
    chatbox.appendChild(msgDiv);
  });
};

// Delete all messages
delBtn.addEventListener('click', () => {
  fetch('http://localhost:5000/api/delete_all', { method: 'DELETE' })
    .then(() => {
      getAndSortMessages();
      delBtn.style.display = "none";
      location.reload();
    });
});

// Initialize the conversation when the DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  getAndSortMessages();

  if (msgInput.value.trim() === '') {
    sendBtn.classList.add('disabled');
    sendBtn.disabled = true;
  } else {
    sendBtn.classList.remove('disabled');
    sendBtn.disabled = false;
  }
});
