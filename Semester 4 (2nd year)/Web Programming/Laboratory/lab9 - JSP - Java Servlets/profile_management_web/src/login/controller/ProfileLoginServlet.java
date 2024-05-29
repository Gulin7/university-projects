package login.controller;

import registration.data_access_object.ProfileDAO;
import registration.models.Profile;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.SQLException;

@WebServlet("/login")
public class ProfileLoginServlet extends HttpServlet {
    private ProfileDAO profileDAO = new ProfileDAO();

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // Retrieve username and password from the login form
        String username = request.getParameter("username");
        String password = request.getParameter("password");

        // Check if the user exists in the database
        Profile profile = null;
        try {
            profile = profileDAO.getProfileByUsernameAndPassword(username, password);
        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        }

        if (profile != null) {
            // User exists, set a session attribute to indicate user is logged in
            request.getSession().setAttribute("loggedInProfile", profile);

            // Set a session attribute to indicate successful login
            request.getSession().setAttribute("loginSuccess", true);

            // Redirect to profile_details.jsp
            response.sendRedirect(request.getContextPath() + "/view/profile_details.jsp");
        } else {
            // User does not exist, redirect back to login page with error message
            request.setAttribute("errorMessage", "Invalid username or password");
            RequestDispatcher dispatcher = request.getRequestDispatcher("/view/profile_login.jsp");
            dispatcher.forward(request, response);
        }
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        RequestDispatcher dispatcher = request.getRequestDispatcher("/view/profile_login.jsp");
        dispatcher.forward(request, response);
    }
}

