//  object literals

const mySym = Symbol("key1")

const JsUser = {
    name : "Vishal",
    "full name" : "Vishal g",
    [mySym] : "key1", // way to write symbol in object
    age : 18,
    location : "Himachal",
    email :  "Vishal23gmail.com",
    isLoggedIn : false,
    lastLoginDays : ["monday", "saturday"]

}

// console.log(JsUser.email);
// console.log(JsUser["email"]);
// console.log(JsUser["full name"]);

// console.log(JsUser[mySym]); // correct syntax of printing symbol in object

JsUser.email = "Vishal.maill.com"
// Object.freeze(JsUser)
JsUser.email = "Vishal.Nomaill.com"

// console.log(JsUser.email);


JsUser.greeting = function(){
    console.log("Hello JS user");
    
}
console.log(JsUser.greeting());

// string interpulation
JsUser.greetingTwo = function(){
    console.log(`Hello JS user, ${this.name}`);
}
console.log(JsUser.greetingTwo());







