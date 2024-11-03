<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html>
<head>
  <title>JSP - Hello World</title>
</head>
<body>
<h1><%= "Hello World!" %></h1>
<br/>
<p>Please log in to manage your URLs.</p>
<form action="posts-servlet" method="get">
  <input type="submit" value="See posts">
</form>
<form action="topics-servlet" method="get">
  <input type="submit" value="See topics">
</form>
</body>
</html>
