/*Header*/
window.addEventListener("scroll", function() {
    const header = document.getElementById("header");
    if (window.scrollY > 20) {
        header.classList.add("fixed");
    } else {
        header.classList.remove("fixed");
    }
});

const toggle = document.getElementById('menu-toggle');
    const menu = document.querySelector('.main_menu');
    toggle.addEventListener('click', () => {
    menu.classList.toggle('active');
    });