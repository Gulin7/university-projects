package com.example.jsp_posts_topics.controller;

import com.example.jsp_posts_topics.domain.DbManager;
import com.example.jsp_posts_topics.domain.Post;
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
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.util.ArrayList;
import java.util.List;

@WebServlet(name = "PostsServlet", value = "/posts-servlet")
public class PostsServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        List<Post> postsList = new ArrayList<>();
        List<Topic> topicsList = new ArrayList<>();
        try (Connection conn = DbManager.getConnection()) {
            String sqlPosts = "select * from posts";
            PreparedStatement stmtPosts = conn.prepareStatement(sqlPosts);
            ResultSet rsPosts = stmtPosts.executeQuery();
            while (rsPosts.next()) {
                int id = rsPosts.getInt("id");
                String user = rsPosts.getString("user");
                int topicId = rsPosts.getInt("topicid");
                String text = rsPosts.getString("text");
                int date = rsPosts.getInt("date");
                postsList.add(new Post(id, user, topicId, text, date));
            }

            String sqlTopics = "select * from topics";
            PreparedStatement stmtTopics = conn.prepareStatement(sqlTopics);
            ResultSet rsTopics = stmtTopics.executeQuery();
            while (rsTopics.next()) {
                int id = rsTopics.getInt("id");
                String name = rsTopics.getString("topicname");
                topicsList.add(new Topic(id, name));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        request.setAttribute("posts", postsList);
        request.setAttribute("topics", topicsList);
        request.getRequestDispatcher("/managePosts.jsp").forward(request, response);
    }

    public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String username = request.getParameter("username");
        String topicName = request.getParameter("topic");
        String text = request.getParameter("text");
        LocalDate currentDate = LocalDate.now();
        LocalDate epochDate = LocalDate.of(1970, 1, 1);
        int currentDateInt = (int) ChronoUnit.DAYS.between(epochDate, currentDate);

        try (Connection conn = DbManager.getConnection()) {
            String checkTopicSql = "SELECT id FROM topics WHERE topicname = ?";
            PreparedStatement checkTopicStmt = conn.prepareStatement(checkTopicSql);
            checkTopicStmt.setString(1, topicName);
            ResultSet rs = checkTopicStmt.executeQuery();

            int topicId;
            if (rs.next()) {
                topicId = rs.getInt("id");
            } else {
                String insertTopicSql = "INSERT INTO topics (topicname) VALUES (?)";
                PreparedStatement insertTopicStmt = conn.prepareStatement(insertTopicSql, PreparedStatement.RETURN_GENERATED_KEYS);
                insertTopicStmt.setString(1, topicName);
                insertTopicStmt.executeUpdate();
                ResultSet generatedKeys = insertTopicStmt.getGeneratedKeys();
                if (generatedKeys.next()) {
                    topicId = generatedKeys.getInt(1);
                } else {
                    throw new SQLException("Creating topic failed, no ID obtained.");
                }
            }

            // Insert new post
            String insertPostSql = "INSERT INTO posts (user, topicid, text, date) VALUES (?, ?, ?, ?)";
            PreparedStatement insertPostStmt = conn.prepareStatement(insertPostSql);
            insertPostStmt.setString(1, username);
            insertPostStmt.setInt(2, topicId);
            insertPostStmt.setString(3, text);
            insertPostStmt.setInt(4, currentDateInt);
            insertPostStmt.executeUpdate();

        } catch (SQLException e) {
            e.printStackTrace();
        }
        doGet(request, response);  // Call doGet to display the updated lists
    }
}
