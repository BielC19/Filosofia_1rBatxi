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
    alert('Moltes gracies, has passat la prova amb ' + textosos)
    setTimeout(() => window.close('','_top',''), 1000);
}
const options = document.querySelectorAll('.option');
const result = document.getElementById('result');
const intents = document.getElementById('tryesses');

let proves = 0;
let textosos = proves + ' intents'

options.forEach(option => {
	option.addEventListener('click', () => {
		options.forEach(o => o.disabled = false);
		if (option.dataset.correct === 'true') {
			result.textContent = 'Correct!';
			result.style.color = '#0f0';
		} else {
			result.textContent = 'Incorrect!';
			result.style.color = '#f00';
			option.classList.add('incorrect');
			setTimeout(() => option.classList.remove('incorrect'), 500);
		}
        proves += 1;
        if (proves==1) {
            textosos = proves + ' intent'
        }
        else{
            textosos = proves + ' intents'
        }
        intents.textContent = 'portes ' + textosos
    });
});

/*
const ball = document.getElementById('Wr1');

const screenHeight = screen.availHeight;
let ballTop = screenHeight;

function animateBall() {
    ball.style.position = 'absolute'
    ballTop -= 5;
    for (let index = 0; index < 2; index++) {
        if (ballTop < 0) {
            ballTop = screenHeight - 2;
        }
        ball.style.top = ballTop + 'px';
        
    }
    ball.style.position = 'relative'
}*/