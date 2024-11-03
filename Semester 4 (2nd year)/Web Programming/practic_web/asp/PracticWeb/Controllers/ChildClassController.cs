using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.ConstrainedExecution;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using PracticWeb.DTO;
using PracticWeb.Mapper;
using PracticWeb.Model;

namespace PracticWeb.Controllers
{
    [Route("api/[controller]")]
    [ApiController] 
    public class ChildClassController(Dao context) : ControllerBase
    {
        private readonly Dao _context = context;

        [HttpGet("range")]
        public IActionResult GetAllChildClassesRange(int Start, int End)
        {
            int range = End - Start + 1;
            List<ChildClass> childClasses = _context.ChildClasses.ToList();
            if(range > childClasses.ToArray().Length || Start > End || Start > childClasses.ToArray().Length) {
                return Ok(childClasses);
            }
            return Ok(childClasses.GetRange(Start-1, range));
        }

        [HttpGet]
        public IActionResult GetAllChildClasses()
        {
            return Ok(_context.ChildClasses.ToList());
        }

        [HttpGet("{id}")]
        public IActionResult GetChildClassById(int id)
        {
            ChildClass? ChildClass = _context.ChildClasses.Find(id);
            if (ChildClass == null)
            {
                return NotFound();
            }
            return Ok(ChildClassMapper.ToDTO(ChildClass));
        }

        [HttpDelete("{id}")]
        public IActionResult DeleteChildClass(int id)
        {
            ChildClass? ChildClass = _context.ChildClasses.Find(id);
            if (ChildClass == null)
            {
                return NotFound();
            }
            _context.ChildClasses.Remove(ChildClass);
            _context.SaveChanges();
            return Ok();
        }

        [HttpPut("{id}")]
        public IActionResult UpdateChildClass(int id, [FromBody] ChildClassDTO ChildClassDTO)
        {
            ChildClass ChildClassToUpdate = ChildClassMapper.ToModel(ChildClassDTO);
            _context.ChildClasses.Update(ChildClassToUpdate);
            _context.SaveChanges();
            return Ok(ChildClassMapper.ToDTO(ChildClassToUpdate));
        }

        [HttpPost]
        public IActionResult AddChildClass([FromBody] ChildClassDTO ChildClassDTO, int UserId)
        {
            ChildClass childClass = ChildClassMapper.ToModel(ChildClassDTO);
            ChildClass savedChildClass = _context.ChildClasses.Add(childClass).Entity;
            User? user = _context.Users.Find(UserId);
            if(user == null)
            {
                return NotFound();
            }
            ParentClass parentClass = new ParentClass(0, "Insert Avatar", UserId, user);
            _context.ParentClasses.Add(parentClass);
            _context.SaveChanges();
            return Ok(ChildClassMapper.ToDTO(savedChildClass));
        }

        [HttpPost("many")]
        public IActionResult UpdateManyChildren([FromBody] List<ChildClassDTO> ChildClassDTOs)
        {
            List<ChildClass> childClasses = ChildClassDTOs.Select(ChildClassMapper.ToModel).ToList();
            foreach (ChildClass childClass in childClasses)
            {
                _context.ChildClasses.Update(childClass);
            }
            _context.SaveChanges();
            return Ok(childClasses.Select(ChildClassMapper.ToDTO));
        }
    }
}
