//! Define Callback Functions:
function doubleNummber(number) {
    return (number*2)
}

function sqaureNummber(number) {
    return (number*number)
}

function incrementNummber(number) {
    return (number+=1)
}



//! Define performOperation Function:
function performOperation(num, operation) {
    return operation(num) 
}


//! Call performOperation with Callback Functions:
console.log(performOperation(5,doubleNummber));
console.log(performOperation(5,sqaureNummber));
console.log(performOperation(5,incrementNummber));




