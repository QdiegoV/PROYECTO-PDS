/*Header*/
window.addEventListener("scroll", function() {
    const header = document.getElementById("header");
    if (window.scrollY > 20) {
        header.classList.add("fixed");
    } else {
        header.classList.remove("fixed");
    }
});

/*Formulario*/
const loginForm = document.getElementById('form-login');
const registroForm = document.getElementById('form-registro');
const mostrarRegistro = document.getElementById('mostrar-registro');
const mostrarLogin = document.getElementById('mostrar-login');

mostrarRegistro.addEventListener('click', (e) => {
    e.preventDefault();
    loginForm.classList.add('oculto');
    registroForm.classList.remove('oculto');
});

mostrarLogin.addEventListener('click', (e) => {
    e.preventDefault();
    registroForm.classList.add('oculto');
    loginForm.classList.remove('oculto');
});

loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    window.location.href = "https://ucompensar.edu.co/";
});

//Footer
    const toggle = document.getElementById('menu-toggle');
    const menu = document.querySelector('.main_menu');
    toggle.addEventListener('click', () => {
    menu.classList.toggle('active');
    });