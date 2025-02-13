class Employee {
    constructor(name,email, age, department, position, salary ){
        this.name = name;
        this.email = email;
        this.age = age;
        this.department = department;
        this.position = position;
        this.salary = salary;
    
    }

    introduce() {
        console.log(`Hello, I am ${this.name}, ${this.position}`);
        
    }

    displaySalary() {
        console.log(`${this.salary}`);
        
    }
}

let newEmployee = new Employee ("Ram", "Ram@gmail.com", 22, "xyz", "HR", "$543222")

console.log(newEmployee);

let manager = new Employee ( "shyam", "shyam@gmail.com", 25, "xyz", "manger", "$98765")

console.log(manager);


newEmployee.introduce();
newEmployee.displaySalary();
manager.introduce();
manager.displaySalary();