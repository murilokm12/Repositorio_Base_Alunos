function gerarCartao() {


let  name = document.getElementById('nome').value;
let  email = document.getElementById('email').value;
let  telefone = document.getElementById('telefone').value;

console.log('Suas informações')

document.getElementById('nomeCartao').innerText = name;
document.getElementById('emailCartao').innerText = email;
document.getElementById('telefoneCartao').innerText = telefone;


}
