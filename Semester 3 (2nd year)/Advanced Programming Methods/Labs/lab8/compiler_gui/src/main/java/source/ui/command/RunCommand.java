package source.ui.command;

import source.controller.InterpreterController;
import source.domain.ProgramState;
import source.domain.adts.MyDictionary;
import source.domain.statements.IStatement;
import source.exceptions.InterpreterException;
import source.repository.IRepository;
import source.repository.ProgramsRepository;

public class RunCommand extends Command {
    private final IStatement programStatement;

    public RunCommand(String key, IStatement programStatement)
    {
        super(key, programStatement.toString());
        this.programStatement = programStatement;
    }

    @Override
    public void execute() {
        try {
            programStatement.typeCheck(new MyDictionary<>());
        }
        catch (InterpreterException e)
        {
            System.out.println(e.getMessage());
            return;
        }

        ProgramState currentProgram = new ProgramState(programStatement);
        IRepository repository = new ProgramsRepository("log.txt");
        InterpreterController interpreterController = new InterpreterController(repository);
        interpreterController.addProgram(currentProgram);

        try {
            interpreterController.allSteps();
        }
        catch (InterpreterException e)
        {
            System.out.println(e.getMessage());
        }
    }
}
