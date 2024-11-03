<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>URL Manager</title>
</head>
<body>
<h1>Welcome</h1>
<p>Please log in to manage your URLs.</p>
<form action="login.jsp" method="post">
  <input type="submit" value="Login">
</form>
<br>
<p>As a guest user, you can see the top 3 most popular URLs:</p>
<form action="topUrls.jsp" method="post">
  <input type="submit" value="See top 3">
</form>
</body>
</html>