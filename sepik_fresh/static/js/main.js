// main.js — Interactivity for public pages (Home, About, Contact)

// Mobile hamburger menu toggle
const hamburger = document.getElementById('hamburger');
const navLinks  = document.querySelector('.nav-links');

if (hamburger && navLinks) {
    hamburger.addEventListener('click', () => {
        navLinks.classList.toggle('open');
    });
}

// Contact form — show success message on submit (frontend only)
const contactForm = document.getElementById('contactForm');
if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const success = document.getElementById('formSuccess');
        if (success) {
            success.style.display = 'block';
            contactForm.reset();
        }
    });
}
