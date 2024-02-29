package repository;

import domain.ProgramState;
import repository.IRepository;

import java.util.ArrayList;

public class ProgramsRepository implements IRepository {
    private final ArrayList<ProgramState> programs;

    public ProgramsRepository() {
        programs = new ArrayList<ProgramState>();
    }

    @Override
    public void addProgram(ProgramState programToAdd) {
        if (!programs.isEmpty())
            programs.set(0, programToAdd);
        else
            programs.add(programToAdd);
    }

    @Override
    public ProgramState getCurrentProgram() {
        return programs.get(0);
    }
}
