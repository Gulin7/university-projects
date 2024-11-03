package com.example.proiectweb.controller;

import com.example.proiectweb.domain.DBManager;
import com.example.proiectweb.domain.Url;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

@WebServlet(name = "AddUrlServlet", value = "/add-servlet")
public class AddUrlServlet extends HttpServlet {

    public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session = request.getSession();
        String username = (String) session.getAttribute("user");
        if (username == null) {
            response.sendRedirect("login.jsp");
            return;
        }
        String url = request.getParameter("url");
        try (Connection conn = DBManager.getConnection()) {
            String sql = "INSERT INTO urls (userId, url) VALUES ((SELECT id FROM users WHERE username = ?), ?)";
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setString(1, username);
            stmt.setString(2, url);
            stmt.executeUpdate();

            //response.sendRedirect("manageUrls.jsp");
        } catch (SQLException e) {
            e.printStackTrace();
        }
        doGet(request, response);
    }

    public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        System.out.println("here");
        List<Url> urlList = new ArrayList<>();
        HttpSession session = request.getSession();
        String username = (String) session.getAttribute("user");
        if (username == null) {
            response.sendRedirect("login.jsp");
            return;
        }
        try (Connection conn = DBManager.getConnection()) {
            String sql = "SELECT * FROM urls WHERE userId = (SELECT id FROM users WHERE username = ?)";
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setString(1, username);

            ResultSet rs = stmt.executeQuery();
                while (rs.next()) {
                    int id = rs.getInt("id");
                    String url = rs.getString("url");
                    int userId = rs.getInt("userId");
                    System.out.println(url);
                    urlList.add(new Url(id, userId, url));
                }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        request.setAttribute("urls", urlList);
        request.getRequestDispatcher("/manageUrls.jsp").forward(request, response);
    }
}
