/* =====================================================
   The Butcher – Main JavaScript
   Loaded at bottom of <body> via base.html
   ===================================================== */

'use strict';

// Auto-dismiss alert messages after 5 seconds
document.addEventListener('DOMContentLoaded', function () {
  const alerts = document.querySelectorAll('.alert.alert-dismissible');
  alerts.forEach(function (alert) {
    setTimeout(function () {
      // Use Bootstrap's dismiss method if available
      const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
      if (bsAlert) {
        bsAlert.close();
      }
    }, 5000);
  });
});

// Set the minimum date on all date inputs to today
document.addEventListener('DOMContentLoaded', function () {
  const today = new Date().toISOString().split('T')[0];
  const dateInputs = document.querySelectorAll('input[type="date"]');
  dateInputs.forEach(function (input) {
    if (!input.min) {
      input.min = today;
    }
  });
});

// Confirm before submitting cancel/delete forms that have data-confirm attribute
document.addEventListener('DOMContentLoaded', function () {
  const confirmForms = document.querySelectorAll('form[data-confirm]');
  confirmForms.forEach(function (form) {
    form.addEventListener('submit', function (e) {
      const message = form.getAttribute('data-confirm');
      if (!window.confirm(message)) {
        e.preventDefault();
      }
    });
  });
});

// Navbar active link highlight based on current URL path
document.addEventListener('DOMContentLoaded', function () {
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll('.navbar .nav-link');
  navLinks.forEach(function (link) {
    if (link.getAttribute('href') === currentPath) {
      link.classList.add('active');
    }
  });
});
