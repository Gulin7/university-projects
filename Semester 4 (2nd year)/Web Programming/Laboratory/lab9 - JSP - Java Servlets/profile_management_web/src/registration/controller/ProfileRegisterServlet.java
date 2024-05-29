package registration.controller;

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

@WebServlet("/register")
public class ProfileRegisterServlet extends HttpServlet {
    private ProfileDAO profileDAO = new ProfileDAO();

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        RequestDispatcher dispatcher = request.getRequestDispatcher("/view/profile_register.jsp");
        dispatcher.forward(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String username = request.getParameter("username");
        String password = request.getParameter("password");
        String email = request.getParameter("email");
        String image = request.getParameter("image");
        String age = request.getParameter("age");
        String home  = request.getParameter("home");

        boolean isUsernameExists = false;
        try {
            isUsernameExists = profileDAO.doesUsernameExists(username);
        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

        if (isUsernameExists) {
            // Inform the user that the username is already taken
            request.setAttribute("usernameExistsMessage", "Username is already taken. Please choose another one.");
            RequestDispatcher dispatcher = request.getRequestDispatcher("/view/profile_register.jsp");
            dispatcher.forward(request, response);
            return;
        }


        Profile profile = new Profile();
        profile.setUsername(username);
        profile.setPassword(password);
        profile.setEmail(email);
        profile.setImage(image);
        profile.setAge(Integer.parseInt(age));
        profile.setHome(home);

        try {
            profileDAO.registerProfile(profile);
        } catch (ClassNotFoundException | SQLException e) {
            throw new ServletException(e);
        }

        RequestDispatcher dispatcher = request.getRequestDispatcher("/view/profile_login.jsp");
        dispatcher.forward(request, response);
    }
}
