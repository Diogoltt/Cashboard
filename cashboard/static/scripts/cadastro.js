document.addEventListener("DOMContentLoaded", function () {

    const loginForm = document.getElementById("form-register");

    loginForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const nome = document.getElementById("nome").value;
        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;

        // Busca no localstorage o email e senha armazenados na lista de usuários
        const users = JSON.parse(localStorage.getItem("users")) || [];

        // Verifica se o email e senha correspondem a algum usuário cadastrado
        const user = users.find(user => user.email === email);

        if (user) {
            alert("Usuário já cadastrado!");
        }

        // Se o usuário não existe, adiciona no localstorage
        localStorage.setItem('users', JSON.stringify([...users, {'nome': nome, 'email': email, 'password': password}]));

        window.location.href = "/";
    });
})