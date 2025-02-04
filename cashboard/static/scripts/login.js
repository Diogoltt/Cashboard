document.addEventListener("DOMContentLoaded", function () {

    const loginForm = document.getElementById("form-login");

    loginForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;

        // Busca no localstorage o email e senha armazenados na lista de usuários
        const users = JSON.parse(localStorage.getItem("users")) || [];

        // Verifica se o email e senha correspondem a algum usuário cadastrado
        const user = users.find(user => user.email === email && user.password === password);

        if (!user) {
            alert("Email ou senha incorretos");
            return;
        }
        window.location.href = "/dashboards";
    });
})