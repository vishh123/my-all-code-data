const user = {
    username : "vishal",
    price : 999,

    welcomeMsg : function (){
        console.log(`${this.username}, welcome to website`); //current context ko refer krne ke liye This keyword use kiya jata hai
        console.log(this);
        
    }
  
}
// user.welcomeMsg()

// user.username= "Vishh"
// user.welcomeMsg()

// console.log(this); //node enviorment ismai this ek empty string ko refer krta hai because global ke under koi context hi nhi hai


// function one (){
//     console.log(this.username); //can't use this in function
    
// }
// one()

// const one = () => {
//     let username = "vishal"
//     console.log(this);
    
// }
// one()

// ----arrow function-----//

// basic arrow function
// const addTwo = (num1, num2) => {
//     return num1+num2
// }
// console.log(addTwo(3,4));

// impleset return : don't use parantheses

// const addTwo = (num1, num2) => num1+num2
console.log(addTwo(3,4));
const addTwo = (num1, num2) => ({ username:"vishal"})



// curly braceses use hua toh return keyword likha hoga , parantheses mai nhi likha hota




