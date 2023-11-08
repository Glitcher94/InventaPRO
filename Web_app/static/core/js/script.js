function addUser() {
    const firstName = document.getElementById("firstName").value;
    const lastName = document.getElementById("lastName").value;
    const rol = document.getElementById("rol").value;
    const programa = document.getElementById("programa").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    // Aquí puedes realizar la lógica para guardar los datos en una base de datos o hacer lo que necesites.

    // Agregar el registro a la lista de usuarios.
    const userList = document.getElementById("userList");
    const listItem = document.createElement("li");
    listItem.textContent = `Nombres: ${firstName}, Apellidos: ${lastName},rol: ${rol}, programa: ${programa}, Correo: ${email}`;
    userList.appendChild(listItem);

    // Muestra el mensaje de registro exitoso.
    const registrationMessage = document.getElementById("registrationMessage");
    registrationMessage.style.display = "block";

    // Limpia los campos del formulario.
    document.getElementById("firstName").value = "";
    document.getElementById("lastName").value = "";
    document.getElementById("rol").value = "";
    document.getElementById("programa").value = "";
    document.getElementById("email").value = "";
    document.getElementById("password").value = "";
}
