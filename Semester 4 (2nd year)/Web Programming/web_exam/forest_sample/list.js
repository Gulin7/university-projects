document.getElementById('seefiles').addEventListener('click', async () => {
    const response = await fetch('http://localhost:63342/forest_sample/getFiles.php', {
        method: "GET",
        headers: {
            'Content-Type': 'application/json'
        }
    });

    if (!response.ok) {
        console.error('Network response was not ok', response.statusText);
        return;
    }

    try {
        const listt = await response.json();
        let ull = document.getElementById('lista');
        ull.innerHTML = '';
        listt.forEach(f => {
            let elem = document.createElement('li');
            elem.innerHTML = f.name;
            ull.appendChild(elem);
        });
    } catch (error) {
        console.error('Error parsing JSON:', error);
    }
});

async function getProjects() {
    const response = await fetch('http://localhost:63342/forest_sample/getProjects.php', {
        method: "GET"
    })
    if(!response.ok)
        alert("Not ok");
    const webData = await response.json();
    populateTable(webData);
}

async function populateTable(data) {
    const table = document.getElementById('projectstable');
    for (const s of data) {
        const row = table.insertRow();
        row.insertCell().textContent = s.id;
        row.insertCell().textContent = s.name;
    }
}

window.onload = () => {
    getProjects();
}