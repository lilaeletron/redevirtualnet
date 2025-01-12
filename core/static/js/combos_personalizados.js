const jsonDataElement = document.getElementById("servisos-json");
const dados = JSON.parse(jsonDataElement.textContent);
console.log(dados[0].fields.nome);