fruits = ["apple", "banana", "cherry", "date"]

fruits.forEach(function(fruit) {
    // console.log(fruit.toUpperCase());
    
});

fruits.forEach((fruit)=>{
    // console.log(fruit.toUpperCase());

})

 let totalCharacters = 0

fruits.forEach(function(fruit){
   totalCharacters += fruit.length;
    
})
// console.log(totalCharacters);


let reversedFruits = fruits.map(function(fruit){
    return fruit.split("").reverse().join("");
})
// console.log(reversedFruits);


let reversedFruitsArrow = fruits.map(fruit => fruit.split("").reverse().join(""));

// console.log(reversedFruitsArrow);

let longFruits = fruits.filter(function(fruit){
    return fruit.length>5;
})
// console.log(longFruits);

let longFruitsArrow = fruits.filter((fruit)=>{
    return fruit.length>5;
})
// console.log(longFruitsArrow);


let aFruitsUpper = fruits.filter(function(fruit){
    return fruit.includes("a")
}).map(function(fruit){
    return fruit.toUpperCase()
})
console.log(aFruitsUpper);

aFruitsUpper = fruits.filter(fruit => fruit.includes("a")).map(fruit => fruit.toUpperCase())
console.log(aFruitsUpper);

