// Obtém os elementos do DOM
var modal = document.getElementById("myModal");
var openModalBtn = document.getElementById("openModalBtn");
var closeModalBtn = document.getElementById("closeModalBtn");

// Quando o usuário clica no botão, abre o modal
openModalBtn.onclick = function() {
    modal.style.display = "block";
}

// Quando o usuário clica no "X", fecha o modal
closeModalBtn.onclick = function() {
    modal.style.display = "none";
}

// Quando o usuário clica fora do modal, também fecha
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
