document.addEventListener('DOMContentLoaded', () => {
    console.log("Financial Education Landing Page Loaded");

    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Form submission handler
    const form = document.querySelector('.subscription-form');
    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const email = document.getElementById('email').value;
            alert(`¡Gracias por suscribirte! Hemos enviado un correo de confirmación a ${email}`);
            form.reset();
        });
    }

    // Add scroll effect to header
    const header = document.querySelector('header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.style.background = 'rgba(24, 15, 40, 0.95)';
            header.style.boxShadow = '0 4px 20px rgba(0,0,0,0.2)';
        } else {
            header.style.background = 'rgba(24, 15, 40, 0.8)';
            header.style.boxShadow = 'none';
        }
    });
});
