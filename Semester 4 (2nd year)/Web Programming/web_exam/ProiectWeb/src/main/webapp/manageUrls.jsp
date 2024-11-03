<%@ page import="com.example.proiectweb.domain.Url" %>
<%@ page import="java.util.List" %><%--
  Created by IntelliJ IDEA.
  User: Asus
  Date: 25.05.2024
  Time: 16:10
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
    <h2>Welcome, ${sessionScope.user}</h2>
    <form action="logout-servlet" method="post">
    <input type="submit" value="logout">
    </form>
    <form action="add-servlet" method="post">
        URL: <input type="text" name="url"><br>
        <input type="submit" value="Add URL">
    </form>

    <form action="add-servlet" method="get">
        <input type="submit" value="SEE YOUR URLS">
    </form>
    <h3>Your URLs:</h3>
    <ul>
        <%
            List<Url> urls = (List<Url>) request.getAttribute("urls");
            if (urls != null) {
                for (Url url : urls) {
        %>
        <li>
            <%= url.getUrl() %>
            <form action="delete-servlet" method="post" style="display:inline;">
                <input type="hidden" name="urlId" value="<%= url.getId() %>">
                <input type="submit" value="Delete">
            </form>
        </li>
        <%
                }
            }
        %>
    </ul>
    <form action="top-n-servlet" method="get">
        <input type="number" name="cnt">
        <input type="submit" value="SEE TOP ${cnt}">
    </form>
    <h3>SEE TOP N URLS:</h3>
    <ul>
        <%
            List<Url> turls = (List<Url>) request.getAttribute("turls");
            if (turls != null) {
                for (Url url : turls) {
        %>
        <li>
            <%= url.getUrl() %>
        </li>
        <%
                }
            }
        %>
    </ul>
</body>
</html>
