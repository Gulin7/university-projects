package source.ui.cli;

import source.domain.statements.IStatement;
import source.ui.Examples;
import source.ui.command.ExitCommand;
import source.ui.command.RunCommand;

public class View {
    public void mainMenu()
    {
        TextMenu menu = new TextMenu();

        menu.addCommand(new ExitCommand("0", "exit"));

        int commandIndex = 1;

        for (IStatement currentStatement : Examples.getAllExamples())
        {
            menu.addCommand(new RunCommand(Integer.toString(commandIndex), currentStatement));
            commandIndex++;
        }

        menu.show();
    }
}
