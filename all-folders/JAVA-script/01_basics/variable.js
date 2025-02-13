const accountId = 12345
let accountEmail = "Vishal.gmail.com" 
var accountPassword = "54321"
accountCity = "Himachal"
let accountState

// accountId = 23 // Const variable can't be change

accountEmail = "vishh.123gmail.com"
accountPassword = "2323231"
accountCity = "Delhi"

console.log(accountId);

/* 
prefer not to use var
because of issue in block scope and functional scope
*/

console.table ([accountId, accountEmail, accountPassword, accountCity, accountState])

