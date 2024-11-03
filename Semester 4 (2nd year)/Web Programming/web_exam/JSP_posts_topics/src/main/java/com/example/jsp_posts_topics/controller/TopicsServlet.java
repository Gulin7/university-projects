package com.example.jsp_posts_topics.controller;

import com.example.jsp_posts_topics.domain.DbManager;
import com.example.jsp_posts_topics.domain.Topic;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

@WebServlet(name = "TopicsServlet", value = "/topics-servlet")
public class TopicsServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        List<Topic> topicsList = new ArrayList<>();
        try (Connection conn = DbManager.getConnection()) {
            String sql = "select * from topics";
            PreparedStatement stmt = conn.prepareStatement(sql);
            ResultSet rs = stmt.executeQuery();
            int count = 0;
            while (rs.next() && count < 3 ) {
                count++;
                int id = rs.getInt("id");
                String name = rs.getString("topicname");
                topicsList.add(new Topic(id, name));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        request.setAttribute("topics", topicsList);
        request.getRequestDispatcher("/managePosts.jsp").forward(request, response);
    }
}
