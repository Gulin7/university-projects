package com.example.proiectweb.controller;

import com.example.proiectweb.domain.DBManager;
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

@WebServlet(name = "LoginServlet", value = "/login-servlet")
public class LoginServlet extends HttpServlet {

    public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        System.out.println("Here");
        String username = request.getParameter("username");
        String password = request.getParameter("password");

        try (Connection conn = DBManager.getConnection()) {
            String sql = "SELECT * FROM Users WHERE username = ? AND password = ?";
            ResultSet rs;
            try (PreparedStatement stmt = conn.prepareStatement(sql)) {
                stmt.setString(1, username);
                stmt.setString(2, password);
                rs = stmt.executeQuery();
                if (rs.next()) {
                    HttpSession session = request.getSession();
                    session.setAttribute("user", username);
                    response.sendRedirect("manageUrls.jsp");
                } else {
                    response.sendRedirect("login.jsp?error=Invalid+credentials");
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
