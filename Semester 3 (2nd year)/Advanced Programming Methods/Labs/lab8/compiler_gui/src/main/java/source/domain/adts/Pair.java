package source.domain.adts;

import source.exceptions.InterpreterException;
import source.domain.ProgramState;

public class Pair {
    public final ProgramState program;
    public final InterpreterException thrownException;

    public Pair(ProgramState program, InterpreterException thrownException) {
        this.program = program;
        this.thrownException = thrownException;
    }
}
