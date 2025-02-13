const FirstUL = document.getElementById("list1")
// console.log(FirstUL.firstElementChild.textContent);

FirstItem = FirstUL.firstElementChild

for(let item = FirstItem; item !==null; item= item.nextElementSibling){
    console.log(item.textContent);
    
}
console.log(" ");

const LastUL = document.getElementById("list2")
// console.log(LastUL.lastElementChild.textContent);

reverseItem = LastUL.lastElementChild

for(let item = reverseItem; item !==null; item= item.previousElementSibling){
    console.log(item.textContent);
    
}
console.log(" ");

const list3 = document.getElementById("list3");
const listItems = list3.children; 

for (let i = 0; i < listItems.length; i++) {
    console.log(listItems[i].textContent); 
}








