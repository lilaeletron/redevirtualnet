/**
 * Função Anônima Imediatamente Invocada (IIFE) para Inicialização do Tema
 *
 * Objetivo:
 * - Ler a preferência de tema (claro ou escuro) do usuário armazenada no localStorage.
 * - Aplicar a classe CSS correspondente ao tema escolhido ao elemento raiz (html)
 *   antes do carregamento completo do CSS, evitando flashes indesejados.
 *
 * Funcionamento:
 * - Verifica o localStorage para determinar qual tema o usuário selecionou anteriormente.
 * - Se o tema for "dark", adiciona a classe "dark-theme" ao elemento html.
 * - Caso contrário, adiciona a classe "light-theme".
 * - Dessa forma, o navegador já processa o CSS com o tema correto desde o início.
 *
 * Benefícios:
 * - Remove o flash de cor clara ao carregar a página quando o modo escuro é preferido.
 * - Mantém uma experiência de usuário consistente, respeitando a preferência definida.
 */

