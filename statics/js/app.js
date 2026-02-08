function change_to_sign_up() {
    document.getElementById("sign-up-form").classList.remove("hidden");
    document.getElementById("login-form").classList.add("hidden");
}

function change_to_login() {
    document.getElementById("login-form").classList.remove("hidden");
    document.getElementById("sign-up-form").classList.add("hidden");
}


function changeEyeToOpen() {
    document.getElementById("id_password").setAttribute("type", "text");
    document.getElementById("closeEye").classList.add("hidden");
    document.getElementById("openEye").classList.remove("hidden");
}

function changeEyeToClose() {
    document.getElementById("id_password").setAttribute("type", "password");
    document.getElementById("openEye").classList.add("hidden");
    document.getElementById("closeEye").classList.remove("hidden");
}

async function showChangeName() {
    document.getElementById("update-form").classList.remove("hidden")
    document.getElementById("content").classList.add("hidden")
}

async function showUserDetail() {
    document.getElementById("update-form").classList.add("hidden")
    document.getElementById("content").classList.remove("hidden")
}