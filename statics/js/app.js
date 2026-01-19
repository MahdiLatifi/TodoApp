// async function deleteTodo(todo_id) {
//     let todo = document.getElementById('todo-' + todo_id)
//     if (todo) {
//         todo.classList.add('deleted-todo')
//         todo.innerHTML = "<h3>todo " + todo_id + "</h3>\n" + "<button class=\"delete-btn undo-btn\" type=\"button\" onclick=\"undoTodo(" + todo_id + ")\">✔</button>"
//     }
// }

async function undoTodo(todo_id) {
    let todo = document.getElementById('todo-' + todo_id)
    todo.classList.remove('deleted-todo')
    todo.innerHTML = "<h3>todo " + todo_id + "</h3>\n" + "<button class=\"delete-btn\" type=\"button\" onclick=\"deleteTodo(" + todo_id + ")\">🔘</button>"
}

async function showChangeName() {
    document.getElementById("update-form").classList.remove("hidden")
    document.getElementById("content").classList.add("hidden")
}

async function showUserDetail() {
    document.getElementById("update-form").classList.add("hidden")
    document.getElementById("content").classList.remove("hidden")
}

// async function addTodo() {
//     let title = document.getElementById('title').value;
//
//     let ele = document.getElementById("content")
//     const todo_id = 3
//     ele.innerHTML = "<div class=\"todo\" id=\"todo-1\">\n" + "<h3>" +
//         title +
//         "</h3>\n" + "<button class=\"delete-btn\" type=\"button\" onclick=\"deleteTodo(" +
//         todo_id +
//         ")\">🔘</button>\n" + " </div>" +
//         ele.innerHTML
// }