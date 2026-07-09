document.addEventListener('DOMContentLoaded', function() {
    // Auto-hide toasts after 5 seconds
    const toasts = document.querySelectorAll('.toast');
    toasts.forEach(function(toast) {
        setTimeout(function() {
            toast.classList.remove('show');
            toast.style.opacity = '0';
            setTimeout(function() { toast.remove(); }, 300);
        }, 5000);
    });

    // Initialize Bootstrap tooltips
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    if (tooltipTriggerList.length > 0) {
        [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));
    }

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#') {
                const target = document.querySelector(href);
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({ behavior: 'smooth' });
                }
            }
        });
    });

    // Table row hover effect
    document.querySelectorAll('.table tbody tr').forEach(function(row) {
        row.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.002)';
            this.style.transition = 'transform 0.2s ease';
        });
        row.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    });
});

// Toggle sidebar
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('sidebarOverlay');
    if (sidebar) {
        sidebar.classList.toggle('open');
        if (overlay) overlay.classList.toggle('active');
    }
}

// Toggle preacher names on team leader dashboard
function togglePreacherNames() {
    const countDiv = document.getElementById('preacherCount');
    const namesDiv = document.getElementById('preacherNames');
    const btn = event.target.closest('button');
    if (countDiv.classList.contains('d-none')) {
        countDiv.classList.remove('d-none');
        namesDiv.classList.add('d-none');
        if (btn) btn.innerHTML = '<i class="fas fa-list me-1"></i>Show Names';
    } else {
        countDiv.classList.add('d-none');
        namesDiv.classList.remove('d-none');
        if (btn) btn.innerHTML = '<i class="fas fa-chart-simple me-1"></i>Show Count';
    }
}
