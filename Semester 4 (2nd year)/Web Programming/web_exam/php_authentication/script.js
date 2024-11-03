document.getElementById('login').addEventListener('submit', async (event) =>{
    event.preventDefault();

    const response = await fetch('http://localhost:63342/php_authentication/authenticateUser.php',{
        method: 'POST',
        headers: {
            'Content-type':'application/json'
        },
        body: JSON.stringify({
            username: document.getElementById('username').value,
            password: document.getElementById('password').value
        })
    })
    const message = await response.json();
    if (message.message == 'success') {
        window.location.replace("http://localhost:63342/php_authentication/list.php"); // Redirect to login page after success
    } else {
        alert(message.message);
    }
})