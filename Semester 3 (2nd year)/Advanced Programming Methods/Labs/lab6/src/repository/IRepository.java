package repository;

import ADT.PrgState;
import Controller.MyException;

import java.util.List;

public interface IRepository {
    void add(PrgState e);
    List<PrgState> getPrgList();
    void setPrgList(List<PrgState>list);
    //public PrgState getCrtPrg();
    void logPrgStateExec(PrgState prgState) throws MyException;
}
