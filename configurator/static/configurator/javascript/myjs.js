// Copy button code to clipboard

function copyTextToClipboard() {
    document.getElementById("copy-button").addEventListener("click", function() {
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

