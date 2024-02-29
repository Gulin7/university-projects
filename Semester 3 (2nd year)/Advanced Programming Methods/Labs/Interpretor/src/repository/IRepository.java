package repository;

import ADT.PrgState;
import Controller.MyException;

public interface IRepository {
    void add(PrgState e);

    public PrgState getCrtPrg();
    void logPrgStateExec() throws MyException;
}
