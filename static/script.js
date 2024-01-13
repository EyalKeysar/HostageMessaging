// Example using vanilla JavaScript
document.getElementById("your-form-id").addEventListener("submit", function (event) {
    event.preventDefault();

    const selectedPersonId = document.getElementById("person-select").value;
    const message = document.getElementById("message-input").value;

    // Update the color via AJAX
    fetch(`/update_color/${selectedPersonId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: message }),
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response if needed
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
