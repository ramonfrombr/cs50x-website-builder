let contador = 0;

document.addEventListener("DOMContentLoaded", function () {
    document.querySelector("button").onclick = contar;
});

function contar() {
    contador++;

    if (contador % 10 === 0) {
        alert(`Contador agora é ${contador}`);
    }

    document.querySelector("h1").innerHTML = contador;
}
