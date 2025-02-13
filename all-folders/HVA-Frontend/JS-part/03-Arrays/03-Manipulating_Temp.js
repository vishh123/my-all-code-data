temperatures = [ -3, 14, 22, 5, -10]
temperatures.forEach(function(temperature) {
    // console.log(temperature);
    
});

temperatures.forEach(temperature => {
    // console.log(temperature);
    
});

temperatures.forEach(function(temperature) {
    const fahreheit = (temperature*9/5)+32;
    // console.log(fahreheit);
    
    
    
});

temperatures.forEach(temperature => {
    const fahreheit = (temperature*9/5)+32;
    // console.log(fahreheit);
    
    
});


const temperaturesInFahrenheit = temperatures.map(function(temperature){
    return (temperature * 9/5) + 32
});
// console.log(temperaturesInFahrenheit);


const temperaturesInFahrenheitArrow = temperatures.map(temperature =>{
    return (temperature * 9/5) + 32
});
// console.log(temperaturesInFahrenheitArrow);


const belowFreezing = temperatures.filter(function(temperature){
    return temperature < 0;
})
// console.log(belowFreezing);

const belowFreezingArrow = temperatures.filter(temperature =>{
    return temperature < 0;
})
// console.log(belowFreezingArrow);














//! INTERVIEW QUESTIONS

// let count =0;
// const nums = [0,1,2,3];
// nums.forEach(num=>{
//     if (num){
//         count = count+1;
//     }
// })
// console.log(count);

// const arr = [2,3,4,5]

// // console.log(arr);
// // console.log(arr.slice(0,1)); // [2]

// arr.splice(0,1)
// arr.unshift(8)
// console.log(arr);

// const obj ={
//     a : 1,
//     b : 2,
//     c : 3,
//     "a" : 6,
//     b : 7
// }
// console.log(obj);


// console.log(!"Vishal"); //
// console.log(+false);

// console.log("" == false);
// console.log("" == false);

// console.log(NaN == NaN);
// console.log(NaN === NaN);

// console.log(1 + undefined); // example of NAN

// console.log(typeof typeof 1000);

// const arr = [3,4,5,6,7,8]
// arr[10] = 100
// console.log(arr);



// function myFunc(){

//      xyz = 100
//     console.log(xyz);
    
// }
// console.log(myFunc());


// var xyz = 1 + abc
//  var abc = 100
// console.log(xyz);

// 


// const abc = [1,2,3,4]
// // console.log(delete data);
// // console.log(delete abc);
// // console.log(delete abc[1]);
// const [x,y] =  abc
// console.log(x,y);


// const a = []
// const b = a
// console.log(a == b);
// console.log(a === b);
















