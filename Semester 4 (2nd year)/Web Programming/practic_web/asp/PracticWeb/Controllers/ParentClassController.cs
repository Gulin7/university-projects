using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using PracticWeb.DTO;
using PracticWeb.Mapper;
using PracticWeb.Model;

namespace PracticWeb.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ParentClassController : ControllerBase
    {
        private readonly Dao _context;

        public ParentClassController(Dao context)
        {
            _context = context;
        }

        [HttpGet()]
        public IActionResult ConfirmRequest(int UserId)
        {
            User? user = _context.Users.Find(UserId);
            if (user == null)
            {
                return NotFound();
            }
            ParentClass parentClass = new ParentClass(0, "Update Avatars", UserId, user);
            _context.ParentClasses.Add(parentClass);
            _context.SaveChanges();
            return Ok(ParentClassMapper.ToDTO(parentClass));
        }


    }
}
