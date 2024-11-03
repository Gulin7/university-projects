async function getWebSites() {
    const response = await fetch('http://localhost:63342/php1/getwebs.php', {
        method: "GET"
    })
    if(!response.ok)
        alert("Not ok");
    const webData = await response.json();
    populateTable(webData);
}

async function populateTable(data) {
    const table = document.getElementById('webtable');
    for (const s of data) {
        const row = table.insertRow();
        row.insertCell().textContent = s.id;
        row.insertCell().textContent = s.url;
        const numberResponse = await fetch(`http://localhost:63342/php1/getdocumentcount.php?id=${s.id}`, {
            method: "GET"
        })
        const documentNumber = await numberResponse.json();
        console.log(documentNumber);
        row.insertCell().textContent = parseInt(documentNumber.cnt);
    }
}

document.getElementById('see').addEventListener('click', async () => {
    const response = await fetch('http://localhost:63342/php1/match.php', {
        method: "POST",
        headers: {
            'Content-Type' : 'application/json'
        },
        body: JSON.stringify({keywords: document.getElementById('keywords').value})
    })
    const documentsArray = await response.json();
    console.log(documentsArray);
    let listt = document.getElementById('matches');
    documentsArray.forEach(d => {
        let elem = document.createElement('li');
        elem.innerHTML = d.name;
        listt.appendChild(elem);
    })
})

document.getElementById('formular').addEventListener('submit', async (e) => {
    e.preventDefault();
    const response = await fetch('http://localhost/php1/updatedocument.php', {
        method: "PUT",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            id: document.getElementById('id').value,
            kw1: document.getElementById('keyword1').value,
            kw2: document.getElementById('keyword2').value,
            kw3: document.getElementById('keyword3').value,
            kw4: document.getElementById('keyword4').value,
            kw5: document.getElementById('keyword5').value
        })
    })
    const todisplay = await response.json();
    console.log(todisplay);
    alert(todisplay);
})

window.onload = () => {
    getWebSites();
}