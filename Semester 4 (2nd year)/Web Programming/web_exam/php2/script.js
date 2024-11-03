document.getElementById('login').addEventListener('submit', async (e) => {
    e.preventDefault();
    const response = await fetch('http://localhost:63342/php2/authenticate.php', {
        method: "POST",
        headers: {
            'Content-Type' : 'application/json'
        },
        body: JSON.stringify({
            username: document.getElementById('username').value,
            password: document.getElementById('password').value
        })
    })
    const message = await response.json();
    if(message.message == "success")
        window.location.replace('http://localhost:63342/php2/list.php');
    else
        alert(message.message);
})