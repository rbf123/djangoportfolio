const texts = [
  "Computer Science Student",
  "Software Developer Intern",
  "Data Analytics Extern",
  "Math & ELA Tutor",
  "Math & AP Computer Science Volunteer Coach",
  "Career Changer",
];

let currentTextIndex = 0;
const homeText = document.getElementById("hometext");

function typeText() {
  let currentText = texts[currentTextIndex];
  homeText.textContent = "";
  homeText.classList.add("typing-animation");

  let i = 0;
  const typingInterval = setInterval(() => {
    homeText.textContent += currentText.charAt(i);
    i++;
    if (i > currentText.length) {
      clearInterval(typingInterval);
      setTimeout(() => {
        homeText.classList.remove("typing-animation");
        currentTextIndex = (currentTextIndex + 1) % texts.length;
        setTimeout(typeText, 2000); // Delay before starting the next text
      }, 2000); // Delay after finishing the current text
    }
  }, 100); // Typing speed (adjust as needed)
}

typeText(); // Start the typing animation
