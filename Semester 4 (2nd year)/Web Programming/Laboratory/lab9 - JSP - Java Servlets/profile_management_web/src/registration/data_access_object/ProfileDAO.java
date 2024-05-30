package registration.data_access_object;

import registration.models.Profile;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class ProfileDAO {
    public int registerProfile(Profile profile) throws ClassNotFoundException, SQLException {
        String INSERT_PROFILE_SQL = "insert into profile(username, password, email, image, age, home) values (?, ?, ?, ?, ?, ?);";

        int result = 0;
        Class.forName("com.mysql.jdbc.Driver");

        try(Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/profiles_web_hw8?useSSL=false", "root", "SergiuUTAARAD2003!");
            PreparedStatement preparedStatement = connection.prepareStatement(INSERT_PROFILE_SQL)
        ){
            preparedStatement.setString(1, profile.getUsername());
            preparedStatement.setString(2, profile.getPassword());
            preparedStatement.setString(3, profile.getEmail());
            preparedStatement.setString(4, profile.getImage());
            preparedStatement.setInt(5, profile.getAge());
            preparedStatement.setString(6, profile.getHome());

            System.out.println(preparedStatement);
            result = preparedStatement.executeUpdate();
        } catch (SQLException exception){
            exception.printStackTrace();
        }

        return result;
    }

    public boolean doesUsernameExists(String username) throws ClassNotFoundException, SQLException {
        String SELECT_USERNAME_SQL = "SELECT COUNT(*) FROM profile WHERE username = ?";

        Class.forName("com.mysql.cj.jdbc.Driver");

        try (Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/profiles_web_hw8?useSSL=false&serverTimezone=UTC", "root", "SergiuUTAARAD2003!");
             PreparedStatement preparedStatement = connection.prepareStatement(SELECT_USERNAME_SQL)) {

            preparedStatement.setString(1, username);
            ResultSet resultSet = preparedStatement.executeQuery();
            if (resultSet.next()) {
                int count = resultSet.getInt(1);
                return count > 0;
            }
        }

        return false;
    }

    public boolean doesUserExists(String username, String password) throws ClassNotFoundException, SQLException {
        String SELECT_USER_SQL = "SELECT COUNT(*) FROM profile WHERE username = ? and password = ?;";

        Class.forName("com.mysql.jdbc.Driver");

        try (Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/profiles_web_hw8?useSSL=false", "root", "SergiuUTAARAD2003!");
             PreparedStatement preparedStatement = connection.prepareStatement(SELECT_USER_SQL)) {


            preparedStatement.setString(1, username);
            preparedStatement.setString(2, password);

            ResultSet resultSet = preparedStatement.executeQuery();
            if (resultSet.next()) {
                int count = resultSet.getInt(1);
                return count > 0;
            }
        }

        return false;
    }


    public Profile getProfileByUsernameAndPassword(String username, String password) throws ClassNotFoundException, SQLException {
        String SELECT_PROFILE_SQL = "SELECT * FROM profile WHERE username = ? AND password = ?";
        Profile profile = null;

        Class.forName("com.mysql.cj.jdbc.Driver");

        try (Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/profiles_web_hw8?useSSL=false", "root", "SergiuUTAARAD2003!");
             PreparedStatement preparedStatement = connection.prepareStatement(SELECT_PROFILE_SQL)) {

            preparedStatement.setString(1, username);
            preparedStatement.setString(2, password);

            ResultSet resultSet = preparedStatement.executeQuery();
            if (resultSet.next()) {
                profile = new Profile();
                profile.setId(resultSet.getInt("id"));
                profile.setUsername(resultSet.getString("username"));
                profile.setPassword(resultSet.getString("password"));
                profile.setEmail(resultSet.getString("email"));
                profile.setImage(resultSet.getString("image"));
                profile.setAge(resultSet.getInt("age"));
                profile.setHome(resultSet.getString("home"));
            }
        }

        return profile;
    }


    public List<Profile> getProfilesByUsername(String username) throws ClassNotFoundException, SQLException {
        List<Profile> profiles = new ArrayList<>();
        String SELECT_ALL_PROFILES_SQL = "SELECT * FROM profile";
        String SELECT_PROFILES_SQL = "SELECT * FROM profile WHERE username LIKE ?";

        Class.forName("com.mysql.cj.jdbc.Driver");

        try (Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/profiles_web_hw8?useSSL=false", "root", "SergiuUTAARAD2003!")) {
            String sqlQuery;
            if (!username.isEmpty()) {
                sqlQuery = SELECT_PROFILES_SQL;
            } else {
                sqlQuery = SELECT_ALL_PROFILES_SQL;
            }

            try (PreparedStatement preparedStatement = connection.prepareStatement(sqlQuery)) {
                if (!username.isEmpty()) {
                    preparedStatement.setString(1, "%" + username + "%");
                }

                ResultSet resultSet = preparedStatement.executeQuery();
                while (resultSet.next()) {
                    Profile profile = new Profile();
                    profile.setUsername(resultSet.getString("username"));
                    profile.setPassword(resultSet.getString("password"));
                    profile.setEmail(resultSet.getString("email"));
                    profile.setImage(resultSet.getString("image"));
                    profile.setAge(resultSet.getInt("age"));
                    profile.setHome(resultSet.getString("home"));
                    profiles.add(profile);
                }
            }
        }

        return profiles;
    }



    public List<Profile> getProfilesByEmail(String email) throws ClassNotFoundException, SQLException {
        List<Profile> profiles = new ArrayList<>();
        String SELECT_ALL_PROFILES_SQL = "SELECT * FROM profile";
        String SELECT_PROFILES_SQL = "SELECT * FROM profile WHERE email LIKE ?";

        Class.forName("com.mysql.cj.jdbc.Driver");

        try (Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/profiles_web_hw8?useSSL=false", "root", "SergiuUTAARAD2003!")) {
            String sqlQuery;
            if (!email.isEmpty()) {
                sqlQuery = SELECT_PROFILES_SQL;
            } else {
                sqlQuery = SELECT_ALL_PROFILES_SQL;
            }

            try (PreparedStatement preparedStatement = connection.prepareStatement(sqlQuery)) {
                if (!email.isEmpty()) {
                    preparedStatement.setString(1, "%" + email + "%");
                }

                ResultSet resultSet = preparedStatement.executeQuery();
                while (resultSet.next()) {
                    Profile profile = new Profile();
                    profile.setUsername(resultSet.getString("username"));
                    profile.setPassword(resultSet.getString("password"));
                    profile.setEmail(resultSet.getString("email"));
                    profile.setImage(resultSet.getString("image"));
                    profile.setAge(resultSet.getInt("age"));
                    profile.setHome(resultSet.getString("home"));
                    profiles.add(profile);
                }
            }
        }

        return profiles;
    }



    public List<Profile> getProfilesByHome(String home) throws ClassNotFoundException, SQLException {
        List<Profile> profiles = new ArrayList<>();
        String SELECT_ALL_PROFILES_SQL = "SELECT * FROM profile";
        String SELECT_PROFILES_SQL = "SELECT * FROM profile WHERE home LIKE ?";

        Class.forName("com.mysql.cj.jdbc.Driver");

        try (Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/profiles_web_hw8?useSSL=false", "root", "SergiuUTAARAD2003!")) {
            String sqlQuery;
            if (!home.isEmpty()) {
                sqlQuery = SELECT_PROFILES_SQL;
            } else {
                sqlQuery = SELECT_ALL_PROFILES_SQL;
            }

            try (PreparedStatement preparedStatement = connection.prepareStatement(sqlQuery)) {
                if (!home.isEmpty()) {
                    preparedStatement.setString(1, "%" + home + "%");
                }

                ResultSet resultSet = preparedStatement.executeQuery();
                while (resultSet.next()) {
                    Profile profile = new Profile();
                    profile.setUsername(resultSet.getString("username"));
                    profile.setPassword(resultSet.getString("password"));
                    profile.setEmail(resultSet.getString("email"));
                    profile.setImage(resultSet.getString("image"));
                    profile.setAge(resultSet.getInt("age"));
                    profile.setHome(resultSet.getString("home"));
                    profiles.add(profile);
                }
            }
        }

        return profiles;
    }
}
