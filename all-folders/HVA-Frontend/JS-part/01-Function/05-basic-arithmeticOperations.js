function addNumbers(a, b) {
    return (a+b)
}

function multiplyNumbers(a, b) {
    return (a*b)
}

function subtractNumbers(a, b) {
    return (b-a)
}

function divideNumbers(a, b) {
   if(b ===0){
    return "Error: Division by zero is not allowed.";
   }
   return (a/b)
}


function performArithmetic(num1, num2, operation) {
    operation(num1 , num2)
}


