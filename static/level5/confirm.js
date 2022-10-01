setTimeout(function () {
    const redirect = document.getElementById('redirect');
    const next = redirect.getAttribute('data-next');
    window.location = next;
}, 5000);