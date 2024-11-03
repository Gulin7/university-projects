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

@WebServlet(name = "TopUrlsServlet", value = "/top-servlet")
public class TopUrlsServlet extends HttpServlet {

    public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        System.out.println("here");
        List<Url> urlList = new ArrayList<>();
        try (Connection conn = DBManager.getConnection()) {
            String sql = "select urls.id, urls.url, urls.userId, count(*) from urls group by urls.url order by count(*) desc";
            PreparedStatement stmt = conn.prepareStatement(sql);

            ResultSet rs = stmt.executeQuery();
            int count = 0;
            while (rs.next() && count < 3) {
                count++;
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
        request.getRequestDispatcher("/topUrls.jsp").forward(request, response);
    }
}
