
/**
 * Formats input value of a time field to HH:MM as the user types.
 * Automatically inserts/removes colon when typing
 * Allows only digits and restricts length.
 */
function formatTimeInput(event) {
    const input = event.target;
    let value = input.value;
    let cursorPos = input.selectionStart; 
    let originalValue = value; 

    let digits = value.replace(/[^\d]/g, '');

    if (digits.length > 4) {
        digits = digits.substring(0, 4);
    }

    let targetValue = digits; 

    if (digits.length >= 3) {
        targetValue = digits.substring(0, 2) + ':' + digits.substring(2);
    }

    if (input.value !== targetValue) {
        const lengthDiff = targetValue.length - originalValue.length;
        input.value = targetValue;

        let newCursorPos = cursorPos;
        if (lengthDiff > 0 && targetValue.includes(':') && originalValue.length === 2 && cursorPos === 2) {
           newCursorPos = 3; // move past the newly added colon
        } 
        else {
           newCursorPos = Math.max(0, Math.min(targetValue.length, cursorPos + lengthDiff));
        }

        // ensure cursor position is valid
        newCursorPos = Math.max(0, Math.min(targetValue.length, newCursorPos));

        input.setSelectionRange(newCursorPos, newCursorPos);
    }
}


/**
 * Parses time string in HH:MM format into total minutes from midnight
 * Returns null if format or time is invalid
 * @param {string} timeString - 24 hour time string ("14:30")
 * @returns {number|null} - Total minutes from midnight or null
 */
function parseTimeToMinutes(timeString) {
    if (!timeString || !/^\d{2}:\d{2}$/.test(timeString)) {
        return null; 
    }
    const parts = timeString.split(':');
    const hours = parseInt(parts[0], 10);
    const minutes = parseInt(parts[1], 10);

    if (hours < 0 || hours > 23 || minutes < 0 || minutes > 59) {
        return null; 
    }

    return hours * 60 + minutes;
}

/**
 * Calculates difference between end time and start time in minutes
 * Updates total time input field
 */
function calculateAndUpdateTotalTime() {
    const startTimeInput = document.getElementById('echo_start_time');
    const endTimeInput = document.getElementById('echo_completion_time');
    const totalTimeInput = document.getElementById('echo_total_time_min');

    if (!startTimeInput || !endTimeInput || !totalTimeInput) {
        return;
    }

    const startTimeStr = startTimeInput.value;
    const endTimeStr = endTimeInput.value;

    const startMinutes = parseTimeToMinutes(startTimeStr);
    const endMinutes = parseTimeToMinutes(endTimeStr);

    if (startMinutes !== null && endMinutes !== null) {
        let difference = endMinutes - startMinutes;

        if (difference < 0) {
            difference += 24 * 60;
        }

        totalTimeInput.value = difference;
    } else {
        totalTimeInput.value = '';
    }
}



function initializeTimeFields() {
    const startTimeInput = document.getElementById('echo_start_time');
    const endTimeInput = document.getElementById('echo_completion_time');

    if (startTimeInput) {
        startTimeInput.addEventListener('input', formatTimeInput);
        startTimeInput.addEventListener('input', calculateAndUpdateTotalTime);
        startTimeInput.addEventListener('blur', calculateAndUpdateTotalTime);
    } else {
        console.error("Start time input not found!");
    }


    if (endTimeInput) {
        endTimeInput.addEventListener('input', formatTimeInput);
        endTimeInput.addEventListener('input', calculateAndUpdateTotalTime);
        endTimeInput.addEventListener('blur', calculateAndUpdateTotalTime);
    } else {
        console.error("End time input not found!");
    }

    // run calculation on page load for prefilled values
    calculateAndUpdateTotalTime();
}

document.addEventListener('DOMContentLoaded', () => {
    initializeTimeFields();  
});