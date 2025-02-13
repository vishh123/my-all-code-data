class book{
    constructor(title, author, publisher, year, genre){
        this.title = title;
        this.author = author;
        this.publisher = publisher;
        this.year = year;
        this.genre = genre;

    }

    describe(){
        console.log(`${this.title} - ${this.author} - (${this.year})`);
        
    }

    displayGenre(){
        console.log(`${this.genre}`);
        
    }

}

const classicBook = new book("Pride and Prejudice", "Jane Austen", "T. Egerton", 1813, "Classic");
const sciFiBook = new book("Dune", "Frank Herbert", "Chilton Books", 1965, "Science Fiction")

console.log(classicBook);
console.log(sciFiBook);


classicBook.describe();
classicBook.displayGenre();

sciFiBook.describe();
sciFiBook.displayGenre();

