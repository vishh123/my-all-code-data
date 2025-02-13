// //* Define and Populate the student Object:
// let student = {} ; 

// student.name = "vishal",
// student.email = 'vishal23@gmail.com',
// student.age ="19"

// console.log(student.name)

// //* Update the student Object:
// student.age = "10"
// console.log(student.age)

// //* Add Method and Nested Object to student:

// student.greet = function (){
//     console.log(`hello, ${this.name}`);
    
// }
// student.greet();

// student.address = {
//     country: "India",
//     city: "Delhi",
//     pinCode: "110053"
// }

// console.log(student.address.country);

// student.address.pinCode = "110054"

// console.log(student.address);


// //* Create and Populate the friend Object:
// let friend = {
//     friend_Name : "Ram",
//     email : "Ram@gmail.com",
//     age : "20",
//     address : "dharmshal, hp",

//     greet: function(){
//     console.log(`hello, ${this.friend_Name}`);

//     }
// }

// friend.greet();
// console.log(friend);


// //* Create and Populate the topper Object:

// let topper = {
//     topper_Name : "vishh",
//     email : "Vishh@123",
//     age : "19",
//     address : "Delhi",

//     greet : function(){
//         console.log(`hello, ${this.topper_Name}`);
//     }
// }

// topper.greet()
// console.log(topper);


//* Define and Use the Student Class:

class student {
    constructor(name,email, age, country, city, pinCode){
        this.name = name;
        this.email = email;
        this.age = age;

        this.address = {
            country: country,
            city: city,
            pinCode: pinCode
        }

    }
    greet(){
        console.log(`hello, ${this.name}`);
        
    }

    getFullAddress(){
        return `${this.address.country}, ${this.address.city} - ${this.address.pinCode}`
    }
}


let student1 = new student("Vishal", "Vishal@gmail.com",19, "India", "Delhi", "110053")
let student2 = new student("Ram", "Ram@gmail.com",20, "India", "mumbai", "100050")
let student3 = new student("Shyam", "Shyam@gmail.com",21, "India", "haryana", "100233")

console.log(student1);
console.log(student2);
console.log(student3);

