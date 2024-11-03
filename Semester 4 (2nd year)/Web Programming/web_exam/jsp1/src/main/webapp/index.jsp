<%@ page import="com.example.jsp1.model.Post" %>
<%@ page import="java.util.List" %>
<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html>
<head>
    <title>JSP - Hello World</title>
</head>
<body>
<ul id="lista">

</ul>
<form id="formular">
    <input type="number" id="id" name="id">
    <input type="text" id="user" name="user">
    <input type="number" id="topicid" name="topicid">
    <input type="text" id="text" name="text">
    <input type="submit" value="add">
</form>
<script>
    window.onload = async function(){
        let response = await fetch('http://localhost:8082/jsp1_war_exploded/posts-servlet');
        let result = await response.json();
        let lista = document.getElementById('lista');
        result.forEach(p => {
            console.log(p);
            let elem = document.createElement('li');
            elem.innerHTML = p.text;
            lista.appendChild(elem);
        })
    }
    document.getElementById('formular').addEventListener('submit', async (e) => {
        e.preventDefault();
        let response = await fetch('http://localhost:8082/jsp1_war_exploded/posts-servlet',{
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                id: document.getElementById('id'),
                user: document.getElementById('user'),
                topicid: document.getElementById('topicid'),
                text: document.getElementById('text')
            })
        });
        let result = await response.json();
    })
</script>
</body>
</html>