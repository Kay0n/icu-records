
/**
 * Calculates Body Surface Area (BSA) using Mosteller formula:
 * BSA (m²) = sqrt((height_cm * weight_kg) / 3600)
 * Updates the BSA input field.
 */
function calculateAndUpdateBSA() {
    const heightInput = document.getElementById('height_cm');
    const weightInput = document.getElementById('weight_kg');
    const bsaInput = document.getElementById('bsa');

    if (!heightInput || !weightInput || !bsaInput) {
        console.error("BSA calculation elements (height, weight, or bsa) not found!");
        return;
    }

    const heightCm = parseFloat(heightInput.value);
    const weightKg = parseFloat(weightInput.value);

    if (!isNaN(heightCm) && heightCm > 0 && !isNaN(weightKg) && weightKg > 0) {
        const bsaM2 = Math.sqrt((heightCm * weightKg) / 3600);
        bsaInput.value = bsaM2.toFixed(2); // rounding to 2 decimal places

    } else {
        bsaInput.value = '';
    }
}


function initializeBSAFields() {
    const heightInput = document.getElementById('height_cm');
    const weightInput = document.getElementById('weight_kg');

    if (heightInput) {
        heightInput.addEventListener('input', calculateAndUpdateBSA);
        heightInput.addEventListener('blur', calculateAndUpdateBSA);
    } else {
        console.error("Height input field (height_cm) not found!");
    }

    if (weightInput) {
        weightInput.addEventListener('input', calculateAndUpdateBSA);
        weightInput.addEventListener('blur', calculateAndUpdateBSA);
    } else {
        console.error("Weight input field (weight_kg) not found!");
    }

    calculateAndUpdateBSA();
}

document.addEventListener('DOMContentLoaded', () => {
    initializeBSAFields();  
});