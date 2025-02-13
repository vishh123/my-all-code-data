const element = document.getElementById("myDiv");
console.log(element.textContent);

const allClass = document.getElementsByClassName("myClass");
console.log(allClass.textContent);

for (let i = 0; i < allClass.length; i++) {
  console.log(allClass[i].textContent);
}

const allpTag  = document.getElementsByTagName("p")
console.log(allpTag.textContent);

for (let i = 0; i < allpTag.length; i++) {
    console.log(allpTag[i].textContent);
}

const allSpan = document.querySelectorAll(".highlight")
console.log(allSpan.textContent);

for (let i = 0; i < allSpan.length; i++) {
    console.log(allSpan[i].textContent);
}

const firstSpanBox = document.querySelector(".highlight")
console.log(firstSpanBox.textContent);



