document.addEventListener('DOMContentLoaded', () => {
    // Função para aplicar o tema
    function applyTheme(theme, themeIconElement, themeTextElement) {
        // Determina se o tema é escuro ou claro baseado na configuração ou nas preferências do sistema
        const isDark = theme === 'dark' || (theme === 'auto' && window.matchMedia('(prefers-color-scheme: dark)').matches);
        const isLight = theme === 'light' || (theme === 'auto' && window.matchMedia('(prefers-color-scheme: light)').matches);

        // Remove classes de tema existentes para evitar sobreposição
        document.body.classList.remove('dark-theme', 'light-theme');

        // Aplica a classe de tema conforme a condição
        if (isDark) {
            document.body.classList.add('dark-theme');
        } else if (isLight) {
            document.body.classList.add('light-theme');
        }

        // Mapeamento de ícones e textos para cada modo
        const themeSettings = {
            dark: {
                icon: '<use href="/static/svg/sprite.svg#moon-stars-fill"></use>',
                text: 'Modo Escuro'
            },
            light: {
                icon: '<use href="/static/svg/sprite.svg#sun-fill"></use>',
                text: 'Modo Claro'
            },
            auto: {
                icon: '<use href="/static/svg/sprite.svg#circle-half"></use>',
                text: 'Modo Automático'
            }
        };

        // Define qual é o tema atual com base na condição
        let currentSetting = 'auto';
        if (isDark) currentSetting = 'dark';
        else if (isLight) currentSetting = 'light';

        // Atualiza o ícone do botão e o texto de descrição do tema
        if (themeIconElement) {
            themeIconElement.innerHTML = themeSettings[currentSetting].icon;
        }
        if (themeTextElement) {
            themeTextElement.textContent = themeSettings[currentSetting].text;
        }

        // Salva o tema escolhido no localStorage
        localStorage.setItem('theme', theme);
    }

    // Função para atualizar o botão ativo do menu de seleção de tema
    function updateActiveButton(themeButtons, selectedButton) {
        themeButtons.forEach(button => {
            const isSelected = (button === selectedButton);
            button.classList.toggle('active', isSelected);
            button.setAttribute('aria-pressed', isSelected.toString());
        });
    }

    const themeDropdownButton = document.getElementById('bd-theme');
    if (!themeDropdownButton) return; // Se o botão não existe, sai da função

    const themeButtonsContainer = themeDropdownButton.nextElementSibling;
    if (!themeButtonsContainer) return;
    const themeButtons = themeButtonsContainer.querySelectorAll('button[data-bs-theme-value]');

    const themeIcon = themeDropdownButton.querySelector('.theme-icon-active');
    const themeText = document.getElementById('bd-theme-text');
    const currentTheme = localStorage.getItem('theme') || 'auto';

    // Inicializa o tema com base no último valor salvo ou "auto"
    function initializeTheme(theme) {
        applyTheme(theme, themeIcon, themeText);
        const btnToActivate = Array.from(themeButtons).find(btn => btn.getAttribute('data-bs-theme-value') === theme);
        if (btnToActivate) {
            updateActiveButton(themeButtons, btnToActivate);
        }
    }

    initializeTheme(currentTheme);

    // Ao clicar em um dos botões do menu, atualiza o tema
    themeButtons.forEach(button => {
        button.addEventListener('click', () => {
            const selectedTheme = button.getAttribute('data-bs-theme-value');
            initializeTheme(selectedTheme);
        });
    });

    // Se o tema atual é "auto", monitora mudanças nas preferências do sistema
    if (currentTheme === 'auto') {
        const darkMatchMedia = window.matchMedia('(prefers-color-scheme: dark)');
        const lightMatchMedia = window.matchMedia('(prefers-color-scheme: light)');
        const handleChange = () => initializeTheme('auto');

        darkMatchMedia.addEventListener('change', handleChange);
        lightMatchMedia.addEventListener('change', handleChange);
    }
});

(function () {
    // Exemplo: checar localStorage
    var theme = localStorage.getItem('theme');
    if (theme === 'dark') {
        document.documentElement.classList.add('dark');
    }
})();
