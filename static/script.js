const form = document.getElementById("predictionForm");

form.addEventListener("submit", () => {

    const button = document.querySelector(".predict-btn");

    button.innerHTML = "Analyzing Market...";

    button.style.opacity = "0.8";
});