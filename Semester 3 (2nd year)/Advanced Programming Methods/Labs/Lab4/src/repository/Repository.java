package repository;

import adt.ProgramState;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;

public class Repository implements IRepository{

    private ArrayList<ProgramState> programStates;
    private String logFilePath;

    public Repository(ProgramState state, String filename)
    {
        logFilePath = filename;
        programStates = new ArrayList<ProgramState>();
        programStates.add(state);
    }

    @Override
    public void add(ProgramState e){
        programStates.add(e);
    }
    @Override
    public ProgramState getCrtPrg(int index) {
        return programStates.get(index);
    }

    @Override
    public void logProgramStateExecution() throws IOException {
        try (PrintWriter logFile = new PrintWriter(new BufferedWriter(new FileWriter("C:\\Codes\\university-projects\\Semester 3 (2nd year)\\Advanced Pr Methods\\Labs\\Lab4\\Lab4\\src\\logFile.txt", true)))) {
            logFile.write(programStates.get(0).toString());
            logFile.write("\n\n\n");
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

}
