// generate rndom color

const randomColor = function(){
    const hex = "0123456789ABCDEF"
    let color = '#'

    for(let i=0 ; i<6 ; i++){
        color+= hex[Math.floor(Math.random() * 16)]

    }
    return color
}

let intervalId
const startChangingColor = function(){

    intervalId = setInterval(changeBgColor,1000)
    function changeBgColor(){
        document.body.style.backgroundColor = randomColor() ;
    }
}
const stopChangingColor = function(){
    clearInterval(intervalId);
}

document.querySelector("#Start").addEventListener('click', startChangingColor)

document.querySelector("#Stop").addEventListener('click', stopChangingColor)
