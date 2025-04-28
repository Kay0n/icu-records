

function initializeDeleteButtons(){
    const deleteForms = document.querySelectorAll('.delete-form');
    deleteForms.forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!confirm('Are you sure you want to delete this record? This action cannot be undone.')) {
                event.preventDefault();
            }
        });
    });
}


function initializeSearchBar(){
    const searchInput = document.getElementById('searchInput');
    const tableBody = document.querySelector('#recordsTable tbody');
    const tableRows = tableBody.getElementsByTagName('tr'); 

    searchInput.addEventListener('input', function() {
        const searchTerm = searchInput.value.toLowerCase().trim(); 

        for (let i = 0; i < tableRows.length; i++) {
            const row = tableRows[i];
            const urCell = row.getElementsByTagName('td')[0];

            if (urCell) {
                const urText = urCell.textContent || urCell.innerText; 
                const urTextLower = urText.toLowerCase();
                if (searchTerm === '' || urTextLower.startsWith(searchTerm)) {
                    row.style.display = "";
                } else {
                    row.style.display = "none"; 
                }
            }
        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
    initializeDeleteButtons();
    initializeSearchBar();
});



