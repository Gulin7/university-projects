package com.example.jsp1.controller;

import com.example.jsp1.model.DBManager;
import com.example.jsp1.model.Message;
import com.example.jsp1.model.Post;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;

import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;
import com.google.gson.Gson;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

@WebServlet(name = "PostsServlet",value = "/posts-servlet")
public class PostsServlet extends HttpServlet {
    public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        StringBuilder stringBuilder = new StringBuilder();
        try (BufferedReader reader = request.getReader()) {
            String line;
            while ((line = reader.readLine()) != null) {
                stringBuilder.append(line);
            }
        }

        String requestBody = stringBuilder.toString();
        Gson gson = new Gson();
        Post newPost = gson.fromJson(requestBody, Post.class);

        try (Connection conn = DBManager.getConnection()) {
            String sql = "INSERT INTO posts values(?, ?, ?, ?, ?)";
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setInt(1,newPost.getId());
            stmt.setString(2, newPost.getUser());
            stmt.setInt(3, newPost.getTopicid());
            stmt.setString(4, newPost.getText());
            stmt.setInt(5, 3);
            stmt.executeUpdate();

        } catch (SQLException e) {
            e.printStackTrace();
        }
        List<Post> postsList2 = new ArrayList<>();
        try (Connection conn = DBManager.getConnection()) {
            String sql = "SELECT * FROM posts";
            PreparedStatement stmt = conn.prepareStatement(sql);

            ResultSet rs = stmt.executeQuery();
            while (rs.next()) {
                int id = rs.getInt("id");
                String user = rs.getString("user");
                int topicid = rs.getInt("topicid");
                String text = rs.getString("text");
                int date = rs.getInt("date");
                postsList2.add(new Post(id, user, topicid, text, date));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        Gson gson2 = new Gson();
        String postsJson = gson2.toJson(postsList2);

        // Set response content type to JSON
        response.setContentType("application/json");
        response.setCharacterEncoding("UTF-8");

        // Write JSON to response
        PrintWriter out = response.getWriter();
        out.print(postsJson);
        out.flush();
    }

    public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        System.out.println("here");
        List<Post> postsList = new ArrayList<>();
        try (Connection conn = DBManager.getConnection()) {
            String sql = "SELECT * FROM posts";
            PreparedStatement stmt = conn.prepareStatement(sql);

            ResultSet rs = stmt.executeQuery();
            while (rs.next()) {
                int id = rs.getInt("id");
                String user = rs.getString("user");
                int topicid = rs.getInt("topicid");
                String text = rs.getString("text");
                int date = rs.getInt("date");
                postsList.add(new Post(id, user, topicid, text, date));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        //request.setAttribute("posts", postsList);
        //request.getRequestDispatcher("/index.jsp").forward(request, response);

        Gson gson = new Gson();
        String postsJson = gson.toJson(postsList);

        // Set response content type to JSON
        response.setContentType("application/json");
        response.setCharacterEncoding("UTF-8");

        // Write JSON to response
        PrintWriter out = response.getWriter();
        out.print(postsJson);
        out.flush();
    }

}
