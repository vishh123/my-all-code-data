const button = document.getElementById("btn");

button.addEventListener("click", () => {
  console.log("Button click event executed");
});

const div = document.getElementById("div");

div.addEventListener("mouseover", () => {
  console.log("Mouseover event on div executed");
});


const textInput = document.getElementById("input");
textInput.addEventListener("input",() => {
    console.log("Input event executed");
});