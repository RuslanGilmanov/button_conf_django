// Copy button code to clipboard
document.addEventListener("DOMContentLoaded", function() {
  const copyButton = document.getElementById("copy-button");

  if (copyButton) {
    copyButton.addEventListener("click", function() {
      const buttonCodeElement = document.getElementById("button-code");
      if (buttonCodeElement) {
        const textToCopy = buttonCodeElement.innerText;

        navigator.clipboard.writeText(textToCopy).then(function() {
          alert('"' + textToCopy + '" copied to clipboard!');
        }, function(err) {
          console.error('Failed to copy: ', err);
        });
      } else {
        console.error('Element with id "button-code" not found.');
      }
    });
  }
});


document.addEventListener("DOMContentLoaded", function() {
  const resetButton = document.getElementById("reset-button");

  if (resetButton) {
    resetButton.addEventListener("click", function() {
      document.getElementById('pressel-form').reset();
    });

      } else {
        console.error('Element with id "reset-button" not found.');
      }
    });