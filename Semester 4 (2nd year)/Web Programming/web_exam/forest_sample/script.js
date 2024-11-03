document.getElementById('login').addEventListener('submit', async (event) =>{
    event.preventDefault();

    const response = await fetch('http://localhost:63342/forest_sample/authenticateUser.php',{
        method: 'POST',
        headers: {
            'Content-type':'application/json'
        },
        body: JSON.stringify({
            name: document.getElementById('name').value,
        })
    })
    const message = await response.json();
    if (message.message == 'success') {
        window.location.replace("http://localhost:63342/forest_sample/list.php");
    } else {
        alert(message.message);
    }
})
