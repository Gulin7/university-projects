package ui.command;

import controller.Controller;
import exceptions.ExpressionException;
import exceptions.InterpreterException;
import exceptions.StatementException;

import java.io.IOException;

public class RunCommand extends Command {
    private final Controller interpreterController;

    public RunCommand(String key, String description, Controller interpreterController)
    {
        super(key, description);
        this.interpreterController = interpreterController;
    }

    @Override
    public void execute()
    {
        try
        {
            interpreterController.executeAllStatements();

        }

        catch (IOException | StatementException | ExpressionException | InterpreterException e)
        {
            System.out.println(e.getMessage());
        }
    }
}
