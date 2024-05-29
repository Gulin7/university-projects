package search_profiles;

import registration.data_access_object.ProfileDAO;
import registration.models.Profile;

import java.io.*;
import java.sql.SQLException;
import java.util.List;


import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@WebServlet("/searchProfiles")
public class SearchProfilesServlet extends HttpServlet {
    private ProfileDAO profileDAO = new ProfileDAO();

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException, ServletException {

        RequestDispatcher dispatcher = request.getRequestDispatcher("/view/search_form.jsp");
        dispatcher.forward(request, response);
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // Retrieve search query parameters
        String username = request.getParameter("username");
        String email = request.getParameter("email");
        String home = request.getParameter("home");

        // Perform search operation based on provided criteria
        List<Profile> searchResults = null;
        try {
            if (!username.isEmpty()) {
                searchResults = profileDAO.getProfilesByUsername(username);
            } else if (!email.isEmpty()) {
                searchResults = profileDAO.getProfilesByEmail(email);
            } else if (!home.isEmpty()) {
                searchResults = profileDAO.getProfilesByHome(home);
            }
        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        }

        // Forward search results to JSP for display
        request.setAttribute("searchResults", searchResults);
        RequestDispatcher dispatcher = request.getRequestDispatcher("/view/search_results.jsp");
        dispatcher.forward(request, response);
    }
}