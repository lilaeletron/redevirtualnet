document.addEventListener("DOMContentLoaded", () => {
    const chatContainer = document.getElementById("chat-container");
    const chatToggleBtn = document.getElementById("chat-toggle");
    const chatCloseBtn = document.getElementById("chat-close");
    const chatSendBtn = document.getElementById("chat-send");
    const chatInput = document.getElementById("chat-input");
    const chatMessages = document.getElementById("chat-messages");

    // Toggle Chat Visibility
    chatToggleBtn.addEventListener("click", () => {
        chatContainer.classList.toggle("show");
    });

    chatCloseBtn.addEventListener("click", () => {
        chatContainer.classList.remove("show");
    });

    // Send Message
    chatSendBtn.addEventListener("click", () => {
        const message = chatInput.value.trim();
        if (message) {
            const userMessage = document.createElement("div");
            userMessage.className = "text-end bg-primary text-white rounded p-2 mb-2";
            userMessage.textContent = message;

            chatMessages.appendChild(userMessage);
            chatMessages.scrollTop = chatMessages.scrollHeight;
            chatInput.value = "";

            // Simulated Bot Response
            setTimeout(() => {
                const botMessage = document.createElement("div");
                botMessage.className = "text-start bg-light text-dark rounded p-2 mb-2";
                botMessage.textContent = "Recebi sua mensagem!";
                chatMessages.appendChild(botMessage);
                chatMessages.scrollTop = chatMessages.scrollHeight;
            }, 1000);
        }
    });
});
