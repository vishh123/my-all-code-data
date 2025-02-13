// Array

const myarr =  [0,1,2,3,4,5]
const myHeors = ["Thor", "Hulk", "spiderman"]

const myArr2 = new Array(1,2,3,4,5)
// console.log(myarr[1]);

// Array Methods

myarr.push(6) //add element in the array
myarr.pop() // remove the last digit in array

myarr.unshift(9) // insert element in the first
myarr.shift() // remove first digit in the array
// console.log(myarr);

// console.log(myarr.indexOf(4));

const newArr = myarr.join() // add array and convert it into string

// console.log(newArr);
// console.log(typeof newArr);

// SLICE, SPLICE

console.log("A ", myarr);
 const myn1 = myarr.slice(1,3)
 console.log(myn1);
 
 console.log("B ", myarr);
 const myn2 = myarr.splice(1,3)

 console.log("C ", myarr);
 console.log(myn2);

//  diffrence B/W
//  Splice manuplate the original array it remove the splice porsion/the parameter value and show the rest.
//  Also splice includes the last range and slice don't includes




 
 



