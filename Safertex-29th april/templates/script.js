document.addEventListener('DOMContentLoaded', function () {
    // Fetch data from SQLite database
    fetch('/query')
        .then(response => response.json())
        .then(data => {
            // Display query results
            const resultsDiv = document.getElementById('results');
            data.forEach(row => {
                const address = document.createElement('p');
                address.textContent = `Location ID: ${row[0]}, Street Address: ${row[1]}, Postal Code: ${row[2]}, City: ${row[3]}, State/Province: ${row[4]}, Country Name: ${row[5]}`;
                resultsDiv.appendChild(address);
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});
