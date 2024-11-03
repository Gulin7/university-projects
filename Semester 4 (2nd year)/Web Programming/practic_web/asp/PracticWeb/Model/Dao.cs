using Microsoft.EntityFrameworkCore;


namespace PracticWeb.Model
{
    public class Dao(DbContextOptions<Dao> options) : DbContext(options)
    {
        public DbSet<ParentClass> ParentClasses { get; set; }
        public DbSet<ChildClass> ChildClasses { get; set; }

        public DbSet<User> Users { get; set; }
    }
}
