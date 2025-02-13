// DOM --> document object model
// kisi document ke element ki class ko select krne ke liye document.getElementById("ID NAME").className likhte hai because document behind the scence usko classname ki smjhta hai.

// to get the attribute we write .getAttribute("Attri name")
// to set the attribute we write .setAttribute("Attri name", "value") : always overright.

// diffrence between innerText and innerContent
//innerText: mai vo content vo show hota hai jo wegpage pr visible hai.
// textContent: ke under sara content ata hai jo kisi display property ki wajh se show nhi ho hota.

//innerHTML: ye content ke saath sath pura html ka value bi show krta hai.it support html tags also.

//document.querySelector('h1') :: it select only first h1 tag.

// to select id in querySelector syntax : document.querySelector('#idname')
// to select class in querySelector syntax : document.querySelector('.classname')

// document.querySelectorAll('h1') : it will select all the h1 tags. and it return the NodeList.

// nodelist and htmlCollection are not the pure array but kuch khubiya milti bi hai.

// to add the style in the nodelist the syntax: myH1[0].style.attribute = 'value'

// to convert anything into array we use ::  Array.from("value").
