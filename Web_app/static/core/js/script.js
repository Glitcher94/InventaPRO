document.addEventListener("DOMContentLoaded", function() {
    const productNameInput = document.getElementById("productName");
    const previewName = document.getElementById("previewName");

    const productCategoryInput = document.getElementById("productCategory");
    const previewCategory = document.getElementById("previewCategory");

    const productAmountInput = document.getElementById("productAmount");
    const previewAmount = document.getElementById("previewAmount");

    
    const productUnitTypeInput = document.getElementById("productUnitType");
    const previewUnitType = document.getElementById("previewUnitType");

    const productBuyOrderInput = document.getElementById("productBuyOrder");
    const previewBuyOrder = document.getElementById("previewBuyOrder");

    productNameInput.addEventListener("input", function() {
        previewName.textContent = productNameInput.value;
    });

    productCategoryInput.addEventListener("input", function() {
        previewCategory.textContent = productCategoryInput.value;
    });

    productAmountInput.addEventListener("input", function() {
        previewAmount.textContent = productAmountInput.value;
    });

    productUnitTypeInput.addEventListener("input", function() {
        previewUnitType.textContent = productUnitTypeInput.value;
    });

    productBuyOrderInput.addEventListener("input", function() {
        previewBuyOrder.textContent = productBuyOrderInput.value;
    });
});

// Resto del código para el envío del formulario y manejo de datos
