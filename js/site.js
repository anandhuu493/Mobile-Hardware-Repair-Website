document.addEventListener('DOMContentLoaded', function () {
    const yearNode = document.getElementById('currentYear');
    if (yearNode) {
        yearNode.textContent = new Date().getFullYear();
    }

    const navLinks = document.querySelectorAll('.navbar .nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function () {
            navLinks.forEach(item => item.classList.remove('active'));
            this.classList.add('active');
        });
    });
});
