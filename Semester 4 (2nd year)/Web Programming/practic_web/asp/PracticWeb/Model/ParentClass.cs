using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace PracticWeb.Model
{
    [Table("Logs")]
    public class ParentClass
    {
        [Key]
        public int Id { get; set; }

        public DateTime Date { get; set; }

        public string Text { get; set; }

        public int UserId { get; set; }

        public User User { get; set; }

        public ParentClass(int id, string name, int userId, User user)
        {
            Id = id;
            Text = name;
            UserId = userId;
            User = user;
            Date = DateTime.Now;
        }

        public ParentClass(int id, string name, int userId)
        {
            Id = id;
            Text = name;
            UserId = userId;
            Date = DateTime.Now;
            User = new User();
        }

        public ParentClass(int id, string name)
        {
            Id = id;
            Text = name;
            UserId = 0;
            Date = DateTime.Now;
        }

        public ParentClass()
        {
            Id = 0;
            Text = "";
            UserId = 0;
            Date = DateTime.Now;
        }
    }
}
