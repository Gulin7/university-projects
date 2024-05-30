package logout;

import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;

@WebServlet("/logoutServlet")
public class LogoutServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException {
        HttpSession session = request.getSession(false); // Get the session, if exists
        if (session != null) {
            session.invalidate(); // Invalidate the session
        }

        response.sendRedirect(request.getContextPath() + "/view/profile_login.jsp"); // Redirect to login page
    }
}
