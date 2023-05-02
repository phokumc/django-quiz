
var totalQuestions = document.body.getAttribute('data-total-questions');

$(document).ready(function() {
    var questionIndex = 0; // Keep track of the current question index

    // Show the next question when the Next button is clicked
    $("#nextBtn").click(function() {
        // Hide the current question
        $("#question" + questionIndex).hide();

        // Increment the question index
        questionIndex++;

        // Show the next question
        $("#question" + questionIndex).show();

        // Hide the Next button if it's the last question, and show the Submit button
        if (questionIndex === parseInt(totalQuestions) - 1) {
            $("#nextBtn").hide();
            $("#submitBtn").show();
        }
    });
});

document.querySelector('.footer').innerHTML += new Date().getFullYear();

// Quiz timer count down function
var timeLeft = 61; // in seconds
var countdownElement = document.getElementById("countdown");
var totalQuestions = document.body.getAttribute('data-total-questions');
var questionIndex = 0;

var countdownId = setInterval(function() {
  timeLeft--;
  var minutes = Math.floor(timeLeft / 60);
  var seconds = timeLeft % 60;
  countdownElement.textContent = minutes + ":" + (seconds < 10 ? "0" : "") + seconds;
  if (timeLeft <= 0) {
    clearInterval(countdownId);
    if (questionIndex === parseInt(totalQuestions) - 1) {
      document.getElementById("submitBtn").click(); // simulate click on Submit button
    } else {
      document.getElementById("nextBtn").click(); // simulate click on Next button
    }
  }
}, 1000);

document.getElementById("nextBtn").addEventListener("click", function() {
  clearInterval(countdownId);
  timeLeft = 61;
  questionIndex++;
  countdownId = setInterval(function() {
    timeLeft--;
    var minutes = Math.floor(timeLeft / 60);
    var seconds = timeLeft % 60;
    countdownElement.textContent = minutes + ":" + (seconds < 10 ? "0" : "") + seconds;
    if (timeLeft <= 0) {
      clearInterval(countdownId);
      if (questionIndex === parseInt(totalQuestions) - 1) {
        document.getElementById("submitBtn").click(); // simulate click on Submit button
      } else {
        document.getElementById("nextBtn").click(); // simulate click on Next button
      }
    }
  }, 1000);
});
