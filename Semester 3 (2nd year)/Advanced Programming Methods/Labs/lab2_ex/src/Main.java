import controller.Controller;
import item.Cube;
import item.Sphere;
import repository.IRepository;
import repository.MemoryRepository;
import view.View;

public class Main {
    public static void main(String[] args) {
        MemoryRepository repo = new MemoryRepository();
        Controller controller = new Controller(repo);
        Cube cube = new Cube(28, "cube");
        Sphere sphere = new Sphere(24, "sphere");
        controller.addItem(cube);
        controller.addItem(sphere);
        View view = new View(controller);
        view.run();

    }
}