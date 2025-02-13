let expenses = [
  {
    id: 1,
    name: "watch",
    amount: 100,
    date: "2024-11-1",
  },

  {
    id: 2,
    name: "walking",
    amount: 80,
    date: "2024-11-5",
  },

  {
    id: 3,
    name: "shpping",
    amount: 200,
    date: "2024-11-10",
  },
];

class Expense {
  constructor(id, name, amount, date) {
    this.id = id;
    this.name = name;
    this.amount = amount;
    this.date = date;
  }
}

function displayExpenses(arr) {
  arr.forEach(function (ex) {
    console.log(`${ex.name} - $${ex.amount} (${ex.date})`);
  });
}

function addExpense(id, name, amount, date) {
  let newExpense = new Expense(id, name, amount, date);
  expenses.push(newExpense);
}
addExpense(1, "burger", 50, "2024-11-20");
displayExpenses(expenses);

function updateExpense(id, amount) {
  let ex = expenses.find(function (ex) {
    return ex.id === id;
  });
  ex.amount = amount;
}
updateExpense(1, 200);
displayExpenses(expenses);

function updateExpenseWithMap(id, amount) {
  expenses = expenses.map(function (ex) {
    if (ex.id === id) {
      ex.amount = amount;
    }
    return ex;
  });
}
updateExpenseWithMap(3, 300);
displayExpenses(expenses);

function removeExpense(id) {
  expenses = expenses.filter((ex) => ex.id != id);
}
removeExpense(3);
displayExpenses(expenses);
