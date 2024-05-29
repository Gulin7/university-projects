<%--
  Created by IntelliJ IDEA.
  User: Sergiu
  Date: 5/3/2024
  Time: 4:14 PM
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Register</title>
<%--    <link rel="stylesheet" type="text/css" href="../styles/header.css">--%>
    <script>
        <%-- Define a JavaScript function to display the alert --%>
        function displayAlert(message) {
            alert(message);
        }
    </script>
    <style>
        /* styles.css */

        .header {
            background-color: #333;
            color: #fff;
            padding: 10px;
            text-align: center;
        }

        .header button {
            background-color: #4CAF50;
            border: none;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            cursor: pointer;
            border-radius: 5px;
            transition-duration: 0.4s;
        }

        .header button:hover {
            background-color: #45a049;
        }

    </style>
</head>
<body>
    <div class="header">
        <button onclick="window.location.href='<%= request.getContextPath() %>/login'">Go to Login</button>
    </div>
    <div class="container">
        <h3>Register</h3>
        <form action="<%= request.getContextPath() %>/register" method="post">
            <table style="width: 80%">
                <tr>
                    <td>username: </td>
                    <td>
                        <input type="text" name="username"/>
                    </td>
                </tr>
                <!-- Add an empty div to display the alert message -->
                <tr>
                    <td colspan="2">
                        <div id="alertMessage"></div>
                    </td>
                </tr>
                <tr>
                    <td>password: </td>
                    <td>
                        <input type="text" name="password"/>
                    </td>
                </tr>
                <tr>
                    <td>email: </td>
                    <td>
                        <input type="text" name="email"/>
                    </td>
                </tr>
                <tr>
                    <td>image: </td>
                    <td>
                        <input type="text" name="image"/>
                    </td>
                </tr>
                <tr>
                    <td>age: </td>
                    <td>
                        <input type="text" name="age"/>
                    </td>
                </tr>
                <tr>
                    <td>home: </td>
                    <td>
                        <input type="text" name="home"/>
                    </td>
                </tr>
            </table>
            <input type="submit" value="Submit"/>
        </form>
    </div>

<%-- Check if the request attribute 'usernameExistsMessage' is not null, and if so, display the alert --%>
<% if (request.getAttribute("usernameExistsMessage") != null) { %>
<script>
    displayAlert("<%= request.getAttribute("usernameExistsMessage") %>");
</script>
<% } %>

</body>
</html>
