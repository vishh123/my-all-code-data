let inventory = [
    {
      id:'1',
      title:'A',
      author:'Amit tandan',
      price:'1000',
      quantity:5
    },
    {
      id:'2',
      title:'B',
      author:'Vishvpitama',
      price:'2000',
      quantity:10
    },
    {
      id:4,
      title:'C',
      author:'Kabirdas',
      price:'3000',
      quantity:15
    }
  ]
  
  class Book{
    constructor(id, title, author, price, quantity){
      this.id = id;
      this.title = title;
      this.author = author;
      this.price = price;
      this.quantity = quantity
    }
  }
  
  function displayBooks(arr){
    arr.forEach(function(book){
      console.log( `${book.title} - ${book.author}(${book.price})`)
    })
  }
  displayBooks(inventory);
  
  function addBook(id, title, author, price, quantity){
    let newBook = new Book(id, title, author, price, quantity);
    inventory.push(newBook)
  }
  addBook(4,'D','shukldev',4000,20);
  displayBooks(inventory);
  
  
  function updateBook(id, quantity){
    let book = inventory.find(function(book){
      return book.id === id;
    })
    book.quantity = quantity;
  }
  updateBook(4, 30);
  displayBooks(inventory);
  
  function updateBookWithMap(id, quantity){
    let updatedInventory = inventory.map(function(book){
      if (book.id === id){
        book.quantity = quantity;
      }
      return book;
    })
  }
  
  function removeBook(id){
    inventory = inventory.filter(book => book.id != id);
  }