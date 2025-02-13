//Immediately Invoked Function Expressions (IIFE)


(function chai(){
    //named IIFE
    console.log(`DB CONNECTED`);
    
})();

// () //for function defination
// () //execution call

// in arrow function // without name
((name) =>{
    console.log(`DB CONNECTED TWO ${name}`);
    
})("Vishal")
