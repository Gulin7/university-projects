import controller.Controller;
import repository.ProgramsRepository;
import ui.Ui;

public class Main {
    public static void main(String[] args)
    {
        ProgramsRepository repo = new ProgramsRepository();
        Controller ctrl = new Controller(repo);
        Ui ui = new Ui(ctrl);

        ui.runUi();
    }
}