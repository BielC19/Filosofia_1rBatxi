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
const ball = document.getElementById('Wr1');

const screenHeight = screen.availHeight;
let ballTop = screenHeight;

function animateBall() {
    ball.style.position = 'absolute'
    ballTop -= 5;
    for (let index = 0; index < 2; index++) {
        if (ballTop < 0) {
            ballTop = screenHeight - ;
        }
        ball.style.top = ballTop + 'px';
        requestAnimationFrame(animateBall);
        setTimeout(1000)
    }


}

animateBall();