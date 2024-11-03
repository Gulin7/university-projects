using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace PracticWeb.Model
{
    [Table("Avatar")]
    public class ChildClass
    {
        [Key]
        public int Id { get; set; }

        public string Name { get; set; }


        public int Rank { get; set; }

        public ChildClass(int id, string name, int rank)
        {
            Id = id;
            Name = name;
            Rank = rank;
        }


        public ChildClass()
        {
            Id = 0;
            Name = "";
            Rank = 0;
        }
    }
}
