let tasks = [
  {
    id: 1,
    description: "book",
    dueDate: "1-1-2024",
    status: "done",
  },
  {
    id: 2,
    description: "pen",
    dueDate: "2-2-2024",
    status: "done",
  },
  {
    id: 3,
    description: "notebook",
    dueDate: "3-3-2024",
    status: "pending",
  },
];

class Task {
  constructor(id, description, dueDate, status) {
    this.id = id;
    this.description = description;
    this.dueDate = dueDate;
    this.status = status;
  }
}

function displayTasks(tasks) {
  tasks.forEach((task) => {
    console.log(`${task.description} - ${task.dueDate}(${task.status})`);
  });
}
displayTasks(tasks);

function addTask(id, description, dueDate, status) {
  let newTask = new Task(id, description, dueDate, status);
  tasks.push(newTask);
}

function updateTask(id, status) {
  let task = tasks.find((task) => task.id === id);
  task.status = status;
}
updateTask(3, "done");
displayTasks(tasks);

function updateTaskWithMap(id, status) {
  let updatedTasks = tasks.map((task) => {
    if (task.id === id) {
      task.status = status;
    }
    return task;
  });
  tasks = updatedTasks;
}
updateTaskWithMap(3, "done");
displayTasks(tasks);

function removeTask(id) {
  tasks = tasks.filter((task) => task.id != id);
}
removeTask(1);
displayTasks(tasks);
