
// jo bhi iss if ke ander lika hai vo hai block scope iske bahar ka hai global scope.
// scope ke ander jo bhi likha jata hai vo bahar nhi jana chahiye.
let a = 300
if (true) {
    let a = 10
    const b = 20
    // console.log("INNER: ", a);
    
    var c = 30 // also print outside it is a global scope
}
// console.log(a);
// console.log(b);
// console.log(c);

////-------------------- NESTED SCOPE >>>>>>>>>>

function one(){
    const username = "Vishall"

    function two (){
        const website = "Youtube"
        console.log(username);
        
    }
    // console.log(website); ////can't access outside the fuction

    two() 
    
}
// one()

if (true) {
    const username = "Vishall"
    if (username ==="Vishall") {
        const website = " youtube"
        // console.log(username + website);
        
    }
}

// ################ INTERESTING ####################

// HOISTING
AddOne(5);
 // We can access 
function AddOne (num){
    return num +1
}

// AddTwo(5) // can't access because we store a function in a varibale 
const AddTwo = function (num){
    return num + 2
}
