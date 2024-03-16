const anw1 = document.querySelector('button:nth-child(1)')
const anw2 = document.querySelector('button:nth-child(2)')
const anw3 = document.querySelector('button:nth-child(3)')
const anw4 = document.querySelector('button:nth-child(4)')

const correcte = document.getElementById('alerta')

function customInputAlert() {
    correcte.style.display = 'flex';
};

function tancarA() {
    correcte.style.display = 'none';
}