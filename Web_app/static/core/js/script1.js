document.getElementById("productForm").addEventListener("submit", function (event) {
    event.preventDefault();

    const productId = document.getElementById("productId").value;
    const productName = document.getElementById("productName").value;
    const productCategory = document.getElementById("productCategory").value;

    const productList = document.getElementById("productList");
    const listItem = document.createElement("li");
    listItem.textContent = `ID: ${productId}, Producto: ${productName}, Categoría: ${productCategory}`;
    productList.appendChild(listItem);

    // Limpia los campos del formulario
    document.getElementById("productId").value = "";
    document.getElementById("productName").value = "";
    document.getElementById("productCategory").value = "aseo"; // Establece el valor predeterminado
});
