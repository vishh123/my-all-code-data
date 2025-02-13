const people = [
    { name: "Alice", age: 25 },
    { name: "Bob", age: 30 },
    { name: "Charlie", age: 35 },
    { name: "Diana", age: 40 }
  ];

function calculateAverageAge(people){
    let ages = 0

    people.forEach(person => {
        ages +=person.age
        
    });

    const averageAge = ages/people.length;
    return averageAge
}

const averageAge = calculateAverageAge(people)

console.log(averageAge);

