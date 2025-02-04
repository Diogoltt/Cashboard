// Selecionando o input e os elementos <li> com IDs atualizados
const passwordInput = document.getElementById('password');
const lengthValidate = document.getElementById('length_validate');
const uppercaseValidate = document.getElementById('uppercase_validate');
const numberValidate = document.getElementById('number_validate');
const specialValidate = document.getElementById('special_validate');

// Função genérica para adicionar/remover classes
function toggleClass(element, isValid) {
    element.classList.remove('valid', 'invalid'); // Remove ambas as classes
    element.classList.add(isValid ? 'valid' : 'invalid'); // Adiciona a correta
}

// Função para verificar a senha enquanto o usuário digita
passwordInput.addEventListener('input', () => {
    const password = passwordInput.value;

    // Verifica se a senha tem pelo menos 8 caracteres
    toggleClass(lengthValidate, password.length >= 8);

    // Verifica se a senha tem pelo menos uma letra maiúscula
    toggleClass(uppercaseValidate, /[A-Z]/.test(password));

    // Verifica se a senha tem pelo menos um número
    toggleClass(numberValidate, /\d/.test(password));

    // Verifica se a senha tem pelo menos um caractere especial
    toggleClass(specialValidate, /[!@#$%^&*(),.?":{}|<>-]/.test(password));
});

// ---------------------------------------------------------------------------------------------------------------------------------------

// Seleciona os elementos do DOM
const togglePassword = document.getElementById('toggle-password');

const toggleConfirmPassword = document.getElementById('toggle-confirm-password');
const confirmPasswordInput = document.getElementById('confirm-password');

// Função para alternar a visibilidade da senha
function toggleVisibility(inputElement, toggleIcon) {
    const isPasswordVisible = inputElement.type === 'text';
    inputElement.type = isPasswordVisible ? 'password' : 'text';
    toggleIcon.classList.toggle('bi-eye-fill', isPasswordVisible);
    toggleIcon.classList.toggle('bi-eye-slash-fill', !isPasswordVisible);
}

// Event listeners para os ícones
togglePassword.addEventListener('click', () => toggleVisibility(passwordInput, togglePassword));
toggleConfirmPassword.addEventListener('click', () => toggleVisibility(confirmPasswordInput, toggleConfirmPassword));
