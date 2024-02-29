import Controller.Controller;
import Repository.IRepository;
import Repository.MemoryIRepository;
import View.View;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) {
        IRepository repo = new MemoryIRepository();
        Controller controller = new Controller(repo);
        View view = new View(controller);
        view.run();
    }
}
