/***********************************************************
 * combos_personalizados.js
 * Lógica para a aba "Combos Personalizado".
 ***********************************************************/

// 1) Variáveis globais
let comboAtual = [];

// 2) Carregar combo sugerido
function carregarComboSugerido(comboId) {
  // Pode buscar via AJAX ou ter um JSON local
  // Exemplo: combosSugeridos[comboId] => array de itens
  comboAtual = [ /* ... */ ];
  renderCombo();
}

// 3) Iniciar combo do zero
function iniciarComboDoZero() {
  comboAtual = [];
  renderCombo();
}

// 4) renderCombo()
function renderCombo() {
  // Monta o HTML no #combo-personalizado-container
  // Exibe itens, botões de remover se não locked, etc.
  const container = document.getElementById("combo-personalizado-container");
  if (!container) return;

  if (comboAtual.length === 0) {
    container.innerHTML = "<p>Nenhum serviço selecionado.</p>";
    return;
  }
  // ...
}

// 5) Eventos
document.addEventListener("DOMContentLoaded", () => {
  // Botões "Personalizar"
  document.querySelectorAll('.personalizar-combo-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const comboId = btn.getAttribute('data-combo-id');
      carregarComboSugerido(comboId);
      // Mostra #combo-personalizado-edicao
      document.getElementById('combo-personalizado-edicao').style.display = 'block';
    });
  });

  // Botão "Criar do Zero"
  const btnZero = document.getElementById('btn-criar-do-zero');
  if (btnZero) {
    btnZero.addEventListener('click', () => {
      iniciarComboDoZero();
      document.getElementById('combo-personalizado-edicao').style.display = 'block';
    });
  }

  // Botão "Finalizar"
  const btnFinalizar = document.getElementById('btn-finalizar-combo');
  if (btnFinalizar) {
    btnFinalizar.addEventListener('click', () => {
      // Lógica de finalização
      alert("Combo finalizado! (Exemplo)");
    });
  }
});
