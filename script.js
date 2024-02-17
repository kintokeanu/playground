// Function to animate falling characters into the bin
function animateFallingCharacters(excessCharacters) {
    const garbageBin = document.getElementById('garbageBin');
    for (let i = 0; i < excessCharacters.length; i++) {
      const fallingChar = document.createElement('span');
      fallingChar.innerText = excessCharacters[i];
      fallingChar.classList.add('falling-char');
      fallingChar.style.animationDelay = `${i * 0.1}s`;
      garbageBin.appendChild(fallingChar);
    }
  }
  
  // Event listener for the input field
  document.getElementById('username').addEventListener('input', function(event) {
    const inputText = event.target.value;
    const inputLength = inputText.length;
    const truncatedText = inputText.substring(0, 6);
    const excessCharacters = inputText.substring(6);
  
    // Check if the input exceeds 6 characters
    if (inputLength > 6) {
      event.target.value = truncatedText; // Set the value to the truncated text
      animateFallingCharacters(excessCharacters); // Animate the excess characters falling into the bin
    }
  });
  