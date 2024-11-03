using PracticWeb.DTO;
using PracticWeb.Model;

namespace PracticWeb.Mapper
{
    public class ParentClassMapper
    {
        public static ParentClassDTO ToDTO(ParentClass parent)
        {
            return new ParentClassDTO(parent.Id, parent.Text, parent.UserId);
        }

        public static ParentClass ToModel(ParentClassDTO parentDTO)
        {
            return new ParentClass(parentDTO.Id, parentDTO.Text, parentDTO.UserId);
        }
    }
}
