document.querySelectorAll("div").forEach(div => {
    div.addEventListener("click", function() {
        const colors = ['red', 'blue', 'yellow', 'green'];
        
        let currentColorIndex = colors.indexOf(div.style.backgroundColor);

        div.style.backgroundColor = colors[(currentColorIndex + 1) % colors.length];
    })
})
