package source.repository;

import source.domain.ProgramState;

import java.util.List;

public interface IRepository {
    void addProgram(ProgramState programToAdd);
    List<ProgramState> getAllPrograms();
    void setProgramsList(List<ProgramState> newPrograms);
    void logProgramState(ProgramState currentProgram);
}
