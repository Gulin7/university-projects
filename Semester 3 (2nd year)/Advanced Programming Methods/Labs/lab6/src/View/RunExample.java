package View;

import Controller.Controller;
import java.util.InputMismatchException;
import java.util.Scanner;
import Controller.MyException;

public class RunExample extends Command {
    private Controller ctr;
    public RunExample(String key, String desc, Controller ctr){
        super(key, desc);
        this.ctr=ctr;
    }
    public boolean getDisplayOption(){
        Scanner scanner = new Scanner(System.in);
        int choice = 0;
        boolean return_val = true;
        boolean exit = false;
        while(!exit) {
            try {
                System.out.println("Select if you want all the steps or just the result:");
                System.out.println("1. All");
                System.out.println("2. Just the result");
                System.out.print("Enter your choice: ");
                choice = scanner.nextInt();
                switch (choice) {
                    case 1:
                        return_val = true;
                        exit = true;
                        break;
                    case 2:
                        return_val = false;
                        exit = true;
                        break;
                    default:
                        throw new MyException("Not a valid input, input 1, 2");
                }
            } catch (MyException e) {
                System.out.println(e);
            } catch (InputMismatchException e) {
                System.out.println("Invalid input. Please enter a number.");
                scanner.next();
            }
        }
        return return_val;
    }
    @Override
    public void execute() {
        try{
            boolean flag = getDisplayOption();
            ctr.setFlag(flag);
            ctr.allStep();
        }
        catch (InterruptedException | MyException e) {
            System.out.println(e.getMessage());
        }
    }
}