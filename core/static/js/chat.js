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

document.addEventListener("DOMContentLoaded", () => {
    const serviceDropdown = document.getElementById("serviceDropdown");
    const addServiceButton = document.getElementById("addService");
    const resetButton = document.getElementById("resetServices");
    const selectedServices = document.getElementById("selectedServices");
    const totalPrice = document.getElementById("totalPrice");

    let total = 0;

    // Adicionar Serviço ao Combo
    addServiceButton.addEventListener("click", () => {
        const selectedOption = serviceDropdown.options[serviceDropdown.selectedIndex];

        // Verifica se o cliente selecionou um serviço
        if (!selectedOption || !selectedOption.value) {
            alert("Por favor, selecione um serviço antes de adicionar.");
            return;
        }

        const serviceId = selectedOption.value;
        const serviceName = selectedOption.getAttribute("data-name");
        const servicePrice = parseFloat(selectedOption.getAttribute("data-price"));
        const serviceDescription = selectedOption.getAttribute("data-descricao");

        // Criar item na lista de serviços selecionados
        const listItem = document.createElement("li");
        listItem.className = "list-group-item d-flex justify-content-between align-items-center";
        listItem.innerHTML = `
            <span>
                <strong>📦 ${serviceName}</strong>
                <br>
                <small>✏️ ${serviceDescription || "Sem descrição disponível"}</small>
            </span>
            <div>
                <span class="badge bg-primary rounded-pill">R$ ${servicePrice.toFixed(2)}</span>
                <button class="btn btn-danger btn-sm ms-2 remove-item">❌</button>
            </div>
        `;

        selectedServices.appendChild(listItem);

        // Atualizar total
        total += servicePrice;
        totalPrice.textContent = `Total: R$ ${total.toFixed(2)}`;

        // Adicionar funcionalidade de remover
        const removeButton = listItem.querySelector(".remove-item");
        removeButton.addEventListener("click", () => {
            listItem.remove();
            total -= servicePrice;
            totalPrice.textContent = `Total: R$ ${total.toFixed(2)}`;
        });
    });

    // Resetar Seleção
    resetButton.addEventListener("click", () => {
        selectedServices.innerHTML = "";
        total = 0;
        totalPrice.textContent = `Total: R$ ${total.toFixed(2)}`;
    });
});

