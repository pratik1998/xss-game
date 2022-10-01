function chooseTab(num) {
  // Dynamically load the appropriate image.
  var html = "Image " + parseInt(escape(num)) + "<br>";
  html += "<img src='/static/level3/cloud" + parseInt(escape(num)) + ".jpg' />";
  // html += "<img src='/static/level3/cloud" + num + ".jpg' />";
  $('#tabContent').html(html);

  window.location.hash = num;

  // Select the current tab
  var tabs = document.querySelectorAll('.tab');
  for (var i = 0; i < tabs.length; i++) {
    if (tabs[i].id == "tab" + parseInt(num)) {
      tabs[i].className = "tab active";
      } else {
      tabs[i].className = "tab";
    }
  }

  // Tell parent we've changed the tab
  top.postMessage(self.location.toString(), "*");
}

window.onload = function() { 
  chooseTab(unescape(self.location.hash.substr(1)) || "1");
}

// Extra code so that we can communicate with the parent page
window.addEventListener("message", function(event){
  if (event.source == parent) {
    chooseTab(unescape(self.location.hash.substr(1)));
  }
}, false);

const tab1 = document.getElementById('tab1');
const tab2 = document.getElementById('tab2');
const tab3 = document.getElementById('tab3');

tab1.addEventListener('click', () => {
    chooseTab(1);
});

tab2.addEventListener('click', () => {
    chooseTab(2);
});

tab3.addEventListener('click', () => {
    chooseTab(3);
});