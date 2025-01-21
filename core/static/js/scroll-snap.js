document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('snapContainer');
    if (!container) return; // se não existir, não faz nada

    const sections = container.querySelectorAll('section');
    let currentIndex = 0;    // índice da seção visível
    let isScrolling = false; // flag para evitar múltiplos gatilhos

    function scrollToSection(index) {
        if (index < 0 || index >= sections.length) return;
        isScrolling = true;
        sections[index].scrollIntoView({behavior: 'smooth', block: 'start'});
        currentIndex = index;
        // após 1 segundo, liberamos para novo scroll
        setTimeout(() => {
            isScrolling = false;
        }, 500);
    }

    container.addEventListener('wheel', (event) => {
        // Se já estiver rolando, ignora novos eventos
        if (isScrolling) {
            event.preventDefault();
            return;
        }

        // Se está rolando para baixo, vamos para a próxima seção
        if (event.deltaY > 0) {
            event.preventDefault();
            scrollToSection(currentIndex + 1);
        }
        // Se está rolando para cima, vamos para a seção anterior
        else if (event.deltaY < 0) {
            event.preventDefault();
            scrollToSection(currentIndex - 1);
        }
    }, {passive: true}); // "passive: false" para podermos dar preventDefault()
});
