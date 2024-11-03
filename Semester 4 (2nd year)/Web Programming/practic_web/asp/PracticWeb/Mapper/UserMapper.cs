using PracticWeb.DTO;
using PracticWeb.Model;

namespace PracticWeb.Mapper
{
    public class UserMapper
    {

        public UserMapper() { }

        public static UserDTO ToDTO(User user)
        {
            return new UserDTO(user.Id, user.Username, user.Password);
        }

        public static User ToModel(UserDTO userDTO)
        {
            return new User(userDTO.Id, userDTO.Username, userDTO.Password);
        }
    }
}
