document.addEventListener("DOMContentLoaded", function () {
  setInterval(function () {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/test");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onload = function () {
      if (xhr.status === 200 && xhr.readyState === 4) {
        var emotions = JSON.parse(xhr.responseText);
        var emotionsDiv = document.getElementById("emotions");
        emotionsDiv.innerHTML = "";
        emotions.forEach(function (emotion) {
          var emotionDiv = document.createElement("div");
          emotionDiv.className = "emo";
          var h2 = document.createElement("h2");
          h2.textContent = emotion.label;
          var p1 = document.createElement("p");
          p1.textContent = emotion.example;
          var p2 = document.createElement("p");
          p2.textContent = emotion.explanation;
          var p3 = document.createElement("p");
          p3.textContent = emotion.etymology;
          emotionDiv.appendChild(h2);
          emotionDiv.appendChild(p1);
          emotionDiv.appendChild(p2);
          emotionDiv.appendChild(p3);
          emotionsDiv.appendChild(emotionDiv);
        });
      }
    };
    xhr.send(JSON.stringify(data));
  }, 1000);
});
