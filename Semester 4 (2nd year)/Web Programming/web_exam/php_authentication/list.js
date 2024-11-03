document.getElementById('seefiles').addEventListener('click', async () => {
    const response = await fetch('http://localhost:63342/php_authentication/getFiles.php', {
        method: "GET",
        headers: {
            'Content-Type': 'application/json'
        }
    });
    const listt = await response.json();
    let ull = document.getElementById('lista');
    listt.forEach(f => {
        let elem = document.createElement('li');
        elem.innerHTML = f.filename;
        ull.appendChild(elem);
    })
})