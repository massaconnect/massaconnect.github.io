// Tab Navigation System
function showSection(sectionId) {
    // Hide all content sections
    document.querySelectorAll('.content-section').forEach(section => {
        section.classList.remove('active');
    });
    
    // Show the selected section
    const targetSection = document.getElementById(sectionId);
    if (targetSection) {
        targetSection.classList.add('active');
    }
    
    // Update active nav link
    document.querySelectorAll('.navbar-menu a').forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === '#' + sectionId) {
            link.classList.add('active');
        }
    });
    
    // Scroll to top of content
    window.scrollTo({ top: 0, behavior: 'smooth' });
    
    // Update URL hash without scrolling
    history.pushState(null, null, '#' + sectionId);
}

// Handle navigation clicks
document.addEventListener('DOMContentLoaded', function() {
    // Set up nav link handlers
    document.querySelectorAll('.navbar-menu a[href^="#"]').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const sectionId = this.getAttribute('href').substring(1);
            showSection(sectionId);
        });
    });
    
    // Handle initial load with hash
    const hash = window.location.hash.substring(1);
    if (hash && document.getElementById(hash)) {
        showSection(hash);
    } else {
        // Show home by default
        showSection('home');
    }
    
    // Handle browser back/forward
    window.addEventListener('popstate', function() {
        const hash = window.location.hash.substring(1);
        if (hash && document.getElementById(hash)) {
            showSection(hash);
        } else {
            showSection('home');
        }
    });
});

// Carousel
function scrollCarousel(direction) {
    const carousel = document.getElementById('carousel');
    const scrollAmount = 260;
    carousel.scrollBy({ left: direction * scrollAmount, behavior: 'smooth' });
}

// Copy wallet address
function copyWallet() {
    const address = document.getElementById('wallet-address').textContent;
    const btn = document.getElementById('copy-btn');

    navigator.clipboard.writeText(address).then(() => {
        btn.classList.add('copied');
        btn.innerHTML = '<svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Copied!';
        setTimeout(() => {
            btn.classList.remove('copied');
            btn.innerHTML = '<svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"/></svg> Copy';
        }, 2000);
    });
}
