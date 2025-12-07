document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('cadastroForm');
    const usernameInput = document.getElementById('username');
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');

    const usernameError = document.getElementById('username-error');
    const emailError = document.getElementById('email-error');
    const passwordError = document.getElementById('password-error');

    form.addEventListener('submit', function(event) {
        let isValid = true; 

        usernameError.textContent = '';
        emailError.textContent = '';
        passwordError.textContent = '';

        if (usernameInput.value() === '') { 
            usernameError.textContent = 'O nome de usuário não pode estar vazio.';
            isValid = false;
        }

        if (emailInput.value() === '') {
            emailError.textContent = 'O e-mail não pode estar vazio.';
            isValid = false;
        } else if (!isValidEmail(emailInput.value)) { 
            emailError.textContent = 'Por favor, insira um e-mail válido (ex: seuemail@dominio.com).';
            isValid = false;
        }

        if (passwordInput.value() === '') {
            passwordError.textContent = 'A senha não pode estar vazia.';
            isValid = false;
        }

        if (!isValid) {
            event.preventDefault(); 
        }
    });

    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }
});