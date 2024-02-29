import view.Interpreter;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;


public class Main {
    public static void main(String[] args) throws IOException {
        try (PrintWriter logFile = new PrintWriter(new BufferedWriter(new FileWriter("C:\\Codes\\university-projects\\Semester 3 (2nd year)\\Advanced Pr Methods\\Labs\\Lab4\\Lab4\\src\\logFile.txt", true)))) {
            logFile.write("works :p");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}