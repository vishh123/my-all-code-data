const cart = [
    {name : "Laptop", price : "50000" , quantity : "1"},
    {name : "Mouse", price : "1500" , quantity : "2"},
    {name : "Keyboard", price : "2000" , quantity : "1"}
]

function  calculateTotalPrice(cart){
    Total_price = 0
    cart.forEach(items => {
        Total_price += items.price * items.quantity;
    });

    return Total_price;
}

let total = calculateTotalPrice(cart)
console.log(total);
