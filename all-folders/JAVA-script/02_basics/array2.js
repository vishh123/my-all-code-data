const marvel_heros = ["thor", "spiderman", "hulk"]
const old_heros = ["saktimaan", "naagraaj", "bheem"]

// marvel_heros.push(old_heros)  // it make a array inside a array
// console.log(marvel_heros);
// console.log(marvel_heros[3][2]);

const all_heros_1 = marvel_heros.concat(old_heros)
// console.log(all_heros_1);

// Spread operator
const all_heros = [...marvel_heros, ...old_heros]
// console.log(all_heros);


const another_array = [1,2,3,[4,5,6,],7,[8,9,],[10]]

const real_array = another_array.flat(Infinity) //merge all the element  and make one array
// console.log(real_array);

console.log( Array.isArray("vishal"));
console.log( Array.from("vishal")); // jo bhi value doge usko vo array bna dega

console.log( Array.from({name: "vishal"})); // humko batna pedga ki key se ya value se array banana haii

let score1 = 100
let score2 = 200
let score3 = 300

console.log(Array.of(score1, score2, score3)); // return new array from set of element 

