//! Define Higher Order Function:

// function higherOrderFuncion(num , callback) {
//     callback(num);
// }

//! Define Callback Function and Call Higher Order Function:

// function callbackFunction(number) {
//     console.log(number);
 

// }
// higherOrderFuncion(5,callbackFunction)



//! Call Higher Order Function with a Function Expression as Callback:
// higherOrderFuncion(10, function(number){
//     console.log(number);
    
// })


//! Callback to Log Square of the Number:
// higherOrderFuncion(4, function(){
//     console.log(number*number);
    
// })


//! Callback to Log Sum of Two Numbers:
function newHigherOrderFunction(num1, num2, callback) {
    callback(num1, num2)
}
newHigherOrderFunction(3,7, function(a , b){
    console.log(a+b);

})
