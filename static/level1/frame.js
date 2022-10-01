const query = document.getElementById('query');

query.addEventListener('focus', function () {
    query.value = '';
});