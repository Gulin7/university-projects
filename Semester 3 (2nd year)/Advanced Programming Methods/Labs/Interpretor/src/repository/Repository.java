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
    @Override
    public PrgState getCrtPrg() {
        return repo.get(0);
    }

//    public void logPrgStateExec(PrgState prgState) throws IOException, MyException {
//        PrintWriter logFile = new PrintWriter(new BufferedWriter(new FileWriter(this.logFilePath, true)));
//        logFile.println(prgState.toString());
//        logFile.close();
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
    public void logPrgStateExec() throws MyException {
        try (PrintWriter logFile = new PrintWriter(new BufferedWriter(new FileWriter(logFilePath, true)))) {
            PrgState prgState = getCrtPrg();

            // Log ExeStack
            logFile.println("ExeStack:");
            logFile.println(prgState.getExeStack().toString());

            // Log SymTable
            logFile.println("\nSymTable:");
            logFile.println(prgState.getSymTable().toString());

            // Log Out
            logFile.println("\nOut:");
            logFile.println(prgState.getOut().toString());

            logFile.println("\nHeap:");
            logFile.println(prgState.getHeap().toString());

            if (prgState.getFileTable() != null) {
                logFile.println("\nFileTable:");
                logFile.println(prgState.fileTableToString());
            }
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
