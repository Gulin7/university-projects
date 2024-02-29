package repository;

import domain.ProgramState;

public interface IRepository {
    void addProgram(ProgramState programToAdd);
    ProgramState getCurrentProgram();
}
