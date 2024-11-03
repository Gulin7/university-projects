using PracticWeb.Model;
using static System.Net.Mime.MediaTypeNames;

namespace PracticWeb.DTO
{
    public class ParentClassDTO(int id, string text, int UserId)
    {
        public int Id { get; set; } = id;
        public int UserId { get; set; } = UserId;

        public string Text { get; set; } = text;

    }
}
