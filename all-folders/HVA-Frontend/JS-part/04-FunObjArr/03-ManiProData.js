const products = [
    {id : "123", name : "laptop", category : "electronic" , price : "1000"},
    {id : "321", name : "t-shirt" , category: "cloth", price : "400"},
    {id : "122", name : "book" , category: "stationary", price : "500"},
    {id : "1233", name : "mango" , category: "food", price : "200"},
    {id : "3321", name : "banana" , category: "food", price : "100"}
]

function displayProducts(array) {
    array.forEach(product => {
        console.log(`${product.name} - ${product.price}`);
        
    });
    
}
displayProducts(products)

const tax = 0.10;

const productsWithTax = products.map(product =>({
    id : product.id,
    name : product.name,
    category : product.category,
    productsWithTax : (product.price*(1 + tax))
}));

displayProducts(productsWithTax);


const foodProducts = products.filter(product => product.category === "food")

displayProducts(foodProducts)

const affordable = products.filter(product => product.price <500);
const affordableString = affordable.map(product => `${product.name} - ${product.price}`)

console.log(affordableString);

let Totalprice = 0

products.forEach(product =>{
    Totalprice +=product.price
})

console.log(Totalprice);


