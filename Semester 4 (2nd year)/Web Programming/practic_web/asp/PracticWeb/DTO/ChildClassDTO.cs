

namespace PracticWeb.DTO
{
    public class ChildClassDTO(int id, string name, int rank)
    {
        public int Id { get; set; } = id;
        public string Name { get; set; } = name;

        public int Rank { get; set; } = rank;
    }
}
