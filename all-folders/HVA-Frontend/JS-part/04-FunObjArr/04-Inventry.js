let inventory = [
  {
    id: 1,
    name: "A",
    price: 10,
    quantity: 2,
  },
  {
    id: 1,
    name: "B",
    price: 5,
    quantity: 4,
  },
  {
    id: 3,
    name: "C",
    price: 20,
    quantity: 1,
  },
];

class Product {
  constructor(id, name, price, quantity) {
    this.id = id;
    this.name = name;
    this.price = price;
    this.quantity = quantity;
  }
}

function displayProducts(inventory) {
  inventory.forEach(function (product) {
    console.log(`${product.name} - $${product.price}(${product.quantity})`);
  });
}
displayProducts(inventory);

function addProduct(id, name, price, quantity) {
  let newProduct = new Product(id, name, price, quantity);
  inventory.push(newProduct);
}

function updateProduct(id, quantity) {
  let product = inventory.find(function (product) {
    return product.id === id;
  });
  product.quantity += quantity;
}

function updateProductWithMap(id, quantity) {
  inventory = inventory.map(function (product) {
    if (product.id === id) {
      product.quantity += quantity;
    }
    return product;
  });
}
updateProductWithMap(1, 3);
displayProducts(inventory);

function removeProduct(id) {
  let newInventory = inventory.filter((product) => product.id != id);
  inventory = newInventory;
}
removeProduct(3);
displayProducts(inventory);
