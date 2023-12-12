function getCookie(name) {
    const cookieValue = document.cookie.split(';').find(cookie => {
        return cookie.trim().startsWith(name + '=');
    });

    if (cookieValue) {
        return cookieValue.split('=')[1];
    }

    return null;
}

let isEditing = false;

function toggleEditName(product_id) {
    const span = document.getElementById(`productName_${product_id}`);
    const input = document.getElementById(`newName_${product_id}`);

    if (input.style.display === 'none') {
        span.style.display = 'none';
        input.style.display = 'inline-block';
        input.focus();
    } else {
        const newName = input.value;
        if (newName.trim() !== '') {
            updateName(product_id, newName);
        }
        span.style.display = 'inline-block';
        input.style.display = 'none';
    }
}

function toggleEditQuantity(product_id) {
    const span = document.getElementById(`productQuantity_${product_id}`);
    const input = document.getElementById(`newQuantity_${product_id}`);

    if (input.style.display === 'none') {
        span.style.display = 'none';
        input.style.display = 'inline-block';
        input.focus();
    } else {
        const newQuantity = input.value;
        if (newQuantity.trim() !== '') {
            updateQuantity(product_id, newQuantity);
        }
        span.style.display = 'inline-block';
        input.style.display = 'none';
    }
}

function updateQuantity(product_id) {
    const newQuantity = document.getElementById(`newQuantity_${product_id}`).value;

    const formData = new FormData();
    formData.append('new_quantity', newQuantity);

    fetch(`/core/update_quantity/${product_id}/${newQuantity}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById(`productQuantity_${product_id}`).innerText = data.new_quantity;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function updateName(product_id, newName) {
    const formData = new FormData();
    formData.append('new_name', newName);

    fetch(`/core/update_name/${product_id}/${newName}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById(`productName_${product_id}`).innerText = data.new_name;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

//Volver blancos los logos al ser seleccionados

function toggleButton(button) {
    var activeButtons = document.getElementsByClassName('nav-link active');
    for (var i = 0; i < activeButtons.length; i++) {
        activeButtons[i].classList.remove('active');
    }
    button.classList.add('active');
}
