async function showChangeName() {
    document.getElementById("update-form").classList.remove("hidden")
    document.getElementById("content").classList.add("hidden")
}

async function showUserDetail() {
    document.getElementById("update-form").classList.add("hidden")
    document.getElementById("content").classList.remove("hidden")
}