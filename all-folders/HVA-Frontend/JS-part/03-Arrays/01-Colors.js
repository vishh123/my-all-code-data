let colors = ["red", "green", "blue"]
// console.log(colors[0]);

colors[1] = "yellow"
// console.log(colors[1]);

colors.push("black")
// console.log(colors[colors.length-1]);

i=0
while (i <colors.length){
    // console.log(colors[i]);
    i+=1
}

for (let i = 0; i < colors.length; i++) {
    // console.log(colors[i]);
    
}

for (let color of colors){
    // console.log(color);
    
}

// console.log(typeof colors);
// console.log(colors.length);

// console.log(colors.pop());
// console.log(colors.indexOf("blue"));

// colors.owner = "Vishal"

// console.log(colors);

for(let prop in colors){
    console.log(prop,":" ,colors[prop]);
    
}