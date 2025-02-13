function myfunction (){
  console.log("V");
  console.log("I");
  console.log("S");
  console.log("H");
  console.log("A");
  console.log("L");

}
// myfunction()

function addTwoNumber(number1, number2){

//    let result =  number1 + number2;
//    return result
return number1 + number2
    
}
const result = addTwoNumber(3,4)

// console.log("result: ", result);

function loginUser(username){
    if (username==undefined){
        console.log("Please enter vaild username");
        return
    }
    return `${username} just logged in `
}

// console.log( loginUser("vishal"));
// console.log( loginUser()); // print undefine


// REST operator  ...
function calculateCartPrice(val1,val2,...num1){ //val1 take 200 and val2 take 400 in it rest will come in array
  return num1
}
// console.log(calculateCartPrice(200,400,500));

const user= {
  username : "vishal",
  price : 199
}

function handleObject (anyobject){
  // console.log(`username is ${anyobject.username} and price is ${anyobject.price}`);
  
}
// handleObject(user)

// we can also pass object directly as following:

handleObject(
  {
    username : "vishh",
    price : 999
  
  }
)

const myArr = [200, 400 , 500 ]

function returnvalue (getArr){
return getArr[1]
}

// console.log(returnvalue(myArr));

// can also do as same as object in array(directly pass)
 
// console.log(returnvalue([200,500,400]));

