<%@ page import="com.example.proiectweb.domain.Url" %>
<%@ page import="java.util.List" %><%--
  Created by IntelliJ IDEA.
  User: Asus
  Date: 25.05.2024
  Time: 17:54
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
    <h2>Hey, anonymous user!</h2>
    <form action="top-servlet" method="get">
        <input type="submit" value="SEE TOP 3 URLS">
    </form>
    <ul>
        <%
            List<Url> urls = (List<Url>) request.getAttribute("urls");
            if (urls != null) {
                for (Url url : urls) {
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
