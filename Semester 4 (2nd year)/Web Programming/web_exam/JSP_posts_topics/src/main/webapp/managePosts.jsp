<%@ page import="com.example.jsp_posts_topics.domain.Post" %>
<%@ page import="java.util.List" %>
<%@ page import="com.example.jsp_posts_topics.domain.Topic" %><%--
  Created by IntelliJ IDEA.
  User: Leona
  Date: 6/10/2024
  Time: 7:11 PM
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
<p>list</p>
<ul>
    <%
        List<Post> posts = (List<Post>) request.getAttribute("posts");
        if (posts != null) {
            for (Post post : posts) {
    %>
    <li>
        <%= post.getText() %>
    </li>
    <%
            }
        }
    %>
</ul>

<ul>
    <%
        List<Topic> topics = (List<Topic>) request.getAttribute("topics");
        if (topics != null) {
            for (Topic topic : topics) {
    %>
    <li>
        <%= topic.getTopicName() %>
    </li>
    <%
            }
        }
    %>
</ul>
</body>
</html>
