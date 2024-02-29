package repository;

import ADT.PrgState;
import Controller.MyException;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.LinkedList;
import java.util.List;

public class Repository implements IRepository {
    List<PrgState> repo = new LinkedList<>();

    public List<PrgState> getPrgList(){
        return repo;
    }

    @Override
    public void setPrgList(List<PrgState>list){
        this.repo = list;
    }

    //String logFilePath = "D:\\Facultate\\MAP";
    String logFilePath;

    public Repository(PrgState progStat, String logFilePath) {
        this.repo.add(progStat);
        this.logFilePath = logFilePath;
        clearFile();
    }
    public IRepository getRepo(){
        return null;
        //return  this.repo;
    }
    @Override
    public void add(PrgState e){
        repo.add(e);
    }
//    @Override
//    public PrgState getCrtPrg() {
//        return repo.get(0);
//    }


    public void clearFile() {
        try {
            PrintWriter file = new PrintWriter(new BufferedWriter(new FileWriter(this.logFilePath, false)));
            file.close();
        } catch (IOException var2) {
            System.out.println(var2);
        }

    }

    @Override
    public void logPrgStateExec(PrgState prgState) throws MyException {
        try (PrintWriter logFile = new PrintWriter(new BufferedWriter(new FileWriter(logFilePath, true)))) {
            //PrgState prgState = getCrtPrg();
            logFile.println("\nPrgState Id = " + prgState.getCurrentId());
            logFile.println("___________________");
            logFile.println("|ExeStack |--> " + prgState.getExeStack().toString());
            //logFile.println(prgState.getExeStack().toString());

            logFile.println("|SymTable |--> " + prgState.getSymTable().toString());
            //logFile.println(prgState.getSymTable().toString());

            logFile.println("| Output  |--> " + prgState.getOut().toString());
            //logFile.println(prgState.getOut().toString());

            logFile.println("|  Heap   |--> "+ prgState.getHeap().toString());
            //logFile.println(prgState.getHeap().toString());

            //if (prgState.getFileTable() != null) {
                logFile.println("|FileTable|--> " + prgState.fileTableToString());
               // logFile.println(prgState.fileTableToString());
            //}
        } catch (IOException e) {
            throw new MyException("Error while writing to the log file: " + e.getMessage());
        }
    }

    @Override
    public String toString() {
        return "Repository{" +
                "repo=" + repo +
                '}';
    }
}
