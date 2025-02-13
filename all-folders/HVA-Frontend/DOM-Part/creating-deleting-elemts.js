function addListItem() {
    const  ul = document.getElementById("List")
    const li = document.createElement("li")
    const X = ul.children.length+1
    li.textContent = `New Item ${X}`
    ul.appendChild(li)
    
    
}
document.getElementById("addButton").addEventListener("click", addListItem);


function removeLastListItem() {
    const  ul = document.getElementById("List")
    if (ul.lastElementChild){
        ul.removeChild(ul.lastElementChild)
    }
}
document.getElementById("removeButton").addEventListener("click", removeLastListItem);