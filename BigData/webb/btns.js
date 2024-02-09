//links
const a1 = 'index'
const a2 = 'aproximacio a la solucio'
const a3 = 'beneficis'
const a4 = 'col·laboració'
const a5 = 'ganxo'
const a6 = 'necessitat'
const dicA = [0, a1, a2, a3, a4, a5, a6]
const lletres = ['a','b','c','d','e','f','g','h','i','j','k','l', 'ñ','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];

window.onload = function() {
    for (let i = 6; i >= 1; i--) {
        let elementNul = document.querySelector('ul');
        let nouli = document.createElement('li');
        nouli.setAttribute('id', lletres[i])
        nouli.setAttribute('class', 'licss')
        elementNul.prepend(nouli);

        let elementNli = document.getElementById(lletres[i]);
        let noua = document.createElement('a');
        
        noua.setAttribute('target', '_top');
        noua.setAttribute('href', dicA[i] + '.html');
        noua.innerHTML = dicA[i];

        elementNli.prepend(noua);
    }
}


/// traker
const url = window.location.pathname;
console.log(url)