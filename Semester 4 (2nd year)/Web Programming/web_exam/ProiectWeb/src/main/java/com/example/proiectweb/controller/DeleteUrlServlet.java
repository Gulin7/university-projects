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
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

@WebServlet(name = "DeleteUrlServlet", value = "/delete-servlet")
public class DeleteUrlServlet extends HttpServlet {

    public void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String urlId = req.getParameter("urlId");
        if (urlId != null && !urlId.isEmpty()) {
            try {
                int id = Integer.parseInt(urlId);
                try (Connection conn = DBManager.getConnection()) {
                    String sql = "DELETE FROM urls WHERE id = ?";
                    try (PreparedStatement stmt = conn.prepareStatement(sql)) {
                        stmt.setInt(1, id);
                        int rowsAffected = stmt.executeUpdate();
                        if (rowsAffected > 0) {
                            doGet(req, resp);
                            return;
                        }
                    }
                }
            } catch (NumberFormatException | SQLException e) {
                e.printStackTrace();
            }
        }
        resp.sendRedirect(req.getContextPath() + "/manage-urls");
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
