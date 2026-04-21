// dashboard.js — Interactivity for all dashboard pages

// Sidebar toggle for mobile screens
const sidebarToggle = document.getElementById('sidebarToggle');
const sidebar       = document.getElementById('sidebar');

if (sidebarToggle && sidebar) {
    sidebarToggle.addEventListener('click', () => {
        sidebar.classList.toggle('open');
    });

    // Close sidebar when clicking outside of it on mobile
    document.addEventListener('click', (e) => {
        if (!sidebar.contains(e.target) && !sidebarToggle.contains(e.target)) {
            sidebar.classList.remove('open');
        }
    });
}
