//? Events in JS
// the change in the state of an object is known as an Event.
// changes jo humare code mai hote hai jaise:-
// # agar humare pass koi button hai usko humne click kiya double click kiya toh vo humare event hai.
// events ko hum use krte hai kisi kaam ko trigger krvane ke liye.
// * Mouse Events(click,double click etc.)
// * Keyboard events(Keypress, keyup, keydown)
// * form events(submit etc.)
// * Print event & many more

// button ke liye ek arttibute hai onclick.

// 2type of event handling
// agr humne apne element ko inline handling se handle or uski ko js mai handle kiya hai toh prioprity js wale ko milegi.

// agr humne kisi Element ko ek bar handle kr diya toh usko hum dubara handle nhi kr skte agr kr rhe hai toh vo overwrite kregaa.

//? Event Object
// It is a special object that has details about the event.
// all event handlers have access to the event object's properties and moethods.

Node.event = (e) =>{ // here e is a variable amd we called it also event object.
    //handle here
}
// e.target , e.type , e.clientX , e.cllientY

//? EVENT listeners
// Node.addEventListener(event , callback)
// Node.removeEventListener(event , callback)

