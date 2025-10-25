<script>
  const form = document.getElementById('screener-form');
  const chatWindow = document.getElementById('chat-window');

  function addMessage(text, sender, typing = false) {
    const msg = document.createElement('div');
    msg.classList.add('message', sender);
    if (typing) {
      msg.innerHTML = "";
    } else {
      msg.textContent = text;
    }
    chatWindow.appendChild(msg);
    chatWindow.scrollTop = chatWindow.scrollHeight;
    return msg;
  }

  // Typing effect: reveal text gradually
  function typeText(element, text, speed = 3) {
    let i = 0;
    function typing() {
      if (i < text.length) {
        element.textContent += text.charAt(i);
        i++;
        setTimeout(typing, speed);
        chatWindow.scrollTop = chatWindow.scrollHeight;
      }
    }
    typing();
  }

  // Add typing indicator (three bouncing dots)
  function addTypingIndicator() {
    const indicator = document.createElement('div');
    indicator.classList.add('message', 'bot');
    indicator.innerHTML = `<span class="dot"></span><span class="dot"></span><span class="dot"></span>`;
    chatWindow.appendChild(indicator);
    chatWindow.scrollTop = chatWindow.scrollHeight;
    return indicator;
  }

  function removeTypingIndicator(indicator) {
    if (indicator && indicator.parentNode) {
      indicator.parentNode.removeChild(indicator);
    }
  }

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(form);

    // Show user message instantly
    addMessage(formData.get('message') || 'Submitted details', 'user');

    // Show typing indicator
    const indicator = addTypingIndicator();

    try {
      const response = await fetch('/screen-candidate', {
        method: 'POST',
        body: formData
      });

      const data = await response.json();

      // Remove typing indicator
      removeTypingIndicator(indicator);

      // Add bot message placeholder
      const botMsg = addMessage("", 'bot', true);

      // Build reply text
      const replyText = `📄 ${data.reply}\nFit Score: ${data.fit_score}\nSkills: ${data.skill_match}`;

      // Animate typing
      typeText(botMsg, replyText, 2);
    } catch (err) {
      removeTypingIndicator(indicator);
      addMessage("⚠️ Error contacting server.", 'bot');
    }
  });
</script>

<style>
  /* Typing indicator dots */
  .dot {
    display: inline-block;
    width: 6px;
    height: 6px;
    margin: 0 2px;
    background-color: #e6edf3;
    border-radius: 50%;
    animation: bounce 0.2s infinite;
  }
  .dot:nth-child(2) { animation-delay: 0.1s; }
  .dot:nth-child(3) { animation-delay: 0.1s; }

  @keyframes bounce {
    0%, 80%, 100% { transform: scale(0); }
    40% { transform: scale(1); }
  }
</style>