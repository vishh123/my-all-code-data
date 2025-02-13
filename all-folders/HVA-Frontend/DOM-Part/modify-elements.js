const button = document.getElementById("btn")
const para = document.getElementById("para")

button.addEventListener("click", () =>{
    para.textContent = "Text has been changed!"
})

const div = document.getElementById("text")

div.addEventListener("mouseover", () =>{
    div.style.backgroundColor = 'yellow'
    div.style.color = 'blue'
})

div.addEventListener('mouseout', () => {
    div.style.backgroundColor = ''; 
    div.style.color = ''; 
  });

const btn = document.getElementById("InsertHTML")
const htmlContent = document.getElementById("htmlContent")

btn.addEventListener("click", () =>{
    htmlContent.innerHTML = `
    <h2> New heading </h2>
    <p>This is a dynamically inserted paragraph.</p>
    `

})

const toggle = document.getElementById('toggle');
const toggleBtn = document.getElementById('toggleBtn');

toggleBtn.addEventListener('click', () => {
  if (toggle.style.display === 'none') {
    toggle.style.display = 'block';
  } else {
    toggle.style.display = 'none';
  }
});