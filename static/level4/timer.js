function startTimer(seconds) {
  seconds = parseInt(seconds) || 3;
  setTimeout(function() { 
    window.confirm("Time is up!");
    window.history.back();
  }, seconds * 1000);
}

const loadingGif = document.getElementById('loading-gif');
loadingGif.addEventListener('load', function() {
    const timer = loadingGif.getAttribute('data-timer');
    startTimer(timer);
});
