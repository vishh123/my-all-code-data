//  const tinderUser = new Object()  //this is singleton object

 const tinderUser = {}

 tinderUser.id = "23bine"
 tinderUser.name = "vishh"
 tinderUser.isLoggedIn = false

//  console.log(tinderUser);

//  objects ke under object //nested object
const regularUser = {
    email : "vishh.com",
    fullname : {
        userfullname : {
            firstname : "vishh",
            lastname : "g"
        }
    }
}

// console.log(regularUser.fullname.userfullname.firstname); // syntax to access the nested object

// combine the object
const obj1 = {1: "a", 2: "b"}
const obj2 = {3: "a", 4: "b"}

// const obj3 = {obj1, obj2}  // ye syntax object ke under object laa deta haii

// const obj3 = Object.assign({},obj1,obj2) // we can use empty parentheses to store obj1 and obj2 in it

// spread operator
const obj3 = {...obj1, ...obj2}
// console.log(obj3);



const users = [
    {
        id : 1,
        email : "vishh.gmail.com"
    },
    {
        id : 1,
        email : "vishh.gmail.com"
    }
]

// console.log(users[1].email)

// console.log(tinderUser);

// console.log(Object.keys(tinderUser)); //access key
// console.log(Object.values(tinderUser)); //access value
// console.log(Object.entries(tinderUser));

// console.log(tinderUser.hasOwnProperty("isLoggedIn")); // can aask ki ye property hai ki nhii


// object destructured
const course ={
    courseName : "js",
    price : "999",
    courseInstructor : "hitesh"
}
// course.courseInstructor

const {courseInstructor : teacher} = course
console.log(teacher);


// destructing in react
// const navbar = ({company}) => {

// }

// navbar (company = "vishhh")


//jab bhi humko apna kaam kisi or ke sar pr dalna ho toh usee API bolte hai


// JSON syntax keys value pair are in string
// {
//     "name" : "vishal",
//     "courseName" : "Js in hindi",
//     "price" : "free"

// }

[
    {},
    {},
    {}
]










 