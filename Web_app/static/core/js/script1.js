function updateQuantity(product_id) {
    const newQuantity = document.getElementById(`newQuantity_${product_id}`).value;

    fetch(`/update_quantity/${product_id}/${newQuantity}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ new_quantity: newQuantity }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById(`productQuantity_${product_id}`).innerText = data.new_quantity;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function toggleEditName(product_id) {
    const span = document.getElementById(`productName_${product_id}`);
    const input = document.getElementById(`newName_${product_id}`);

    if (span.style.display !== 'none') {
        span.style.display = 'none';
        input.style.display = 'inline-block';
    } else {
        span.style.display = 'inline-block';
        input.style.display = 'none';
    }
}

function updateName(product_id) {
    const newName = document.getElementById(`newName_${product_id}`).value;

    fetch(`/update_name/${product_id}/${newName}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ new_name: newName }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById(`productName_${product_id}`).innerText = data.new_name;
        toggleEditName(product_id); // Ocultar campo de edición después de actualizar el nombre
    })
    .catch(error => {
        console.error('Error:', error);
    });
}