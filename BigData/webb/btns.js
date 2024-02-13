//links
const a1 = 'index'
const a2 = 'aproximacio a la solucio'
const a3 = 'beneficis'
const a4 = 'col·laboració'
const a5 = 'ganxo'
const a6 = 'necessitat'
const dicA = [0, a1, a2, a3, a4, a5, a6]
const lletres = ['a','b','c','d','e','f','g','h','i','j','k','l', 'ñ','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];

const lletres2 = lletres.reverse();

const url = window.parent.location.pathname;
console.log(url)

window.onload = function() {
    for (let i = 6; i >= 1; i--) {
        let elementNul = document.querySelector('ul');
        let nouli = document.createElement('li');
        nouli.setAttribute('id', lletres[i])
        nouli.setAttribute('class', 'licss')
        elementNul.prepend(nouli);
        
        let elementNLi = document.getElementById(lletres[i]);
        let nouA = document.createElement('a');

        nouA.setAttribute('id', lletres2[i])
        nouA.setAttribute('target', '_top');
        nouA.setAttribute('href', dicA[i]);
        ///nouA.setAttribute('href', dicA[i] + '.html');
        nouA.innerHTML = dicA[i];
        if (url === '/1rBarxiA_BCS/BigData/webb/' + dicA[i]) {
        ///if (url === '/' + dicA[i] + '.html') {
            nouA.setAttribute('id', 'actiu')
        }
/*        else if (url === '/1rBarxiA_BCS/BigData/webb/') {
                nouA.setAttribute('id', 'actiu')
        }
        else if (url === '/1rBarxiA_BCS/BigData/webb/aproximacio%20a%20la%20solucio') {
            ///if (url === '/' + dicA[i] + '.html') {
                nouA.setAttribute('id', 'actiu')
            } */
        elementNLi.prepend(nouA);
    }
}

/// traker