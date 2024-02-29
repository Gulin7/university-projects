package View;

import ADT.PrgState;
import ADT.expresion.ArithExp;
import ADT.expresion.RelationalExp;
import ADT.expresion.VarExp;
import ADT.statement.*;
import ADT.types.BooleanType;
import ADT.types.StringType;
import ADT.value.BoolValue;
import ADT.value.IntValue;
import ADT.value.StringValue;
import ADT.value.Value;
import ADT.dictionary.MyDictionary;
import ADT.dictionary.MyIDictionary;
import ADT.list.MyIList;
import ADT.list.MyList;
import ADT.stack.MyIStack;
import ADT.stack.MyStack;
import Controller.Controller;
import ADT.types.IntType;
import repository.IRepository;
import repository.Repository;
import Controller.MyException;
import ADT.expresion.ValueExp;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.util.InputMismatchException;
import java.util.Scanner;


//public class View {
//    //int v;v=2;Print(v)
//    IStmt ex0 = new CompStmt(new VarDeclStmt("varf", new StringType()),
//            new CompStmt(new AssignStmt("varf", new ValueExp(new StringValue("D:\\Facultate\\MAP\\logfile.txt"))), new PrintStmt(new VarExp("varf"))));
//
//    IStmt ex5 = new CompStmt(new VarDeclStmt("varf", new StringType()),
//            new CompStmt(new AssignStmt("varf", new ValueExp(new StringValue("D:\\Facultate\\MAP\\logfile.txt"))),
//                    new CompStmt(new OpenRFileStmt(new VarExp("varf")),
//                            new CompStmt(new VarDeclStmt("varc", new IntType()),
//                                    new CompStmt(new ReadFileStmt(new VarExp("varf"), "varc"),
//                                            new CompStmt(new PrintStmt(new VarExp("varc")),
//                                                    new CloseRFileStmt(new VarExp("varf"))) )))));
//
//    //int a; int b; a = 2; b = 2 print(a==b)
//    IStmt ex1 = new CompStmt(new VarDeclStmt("a", new IntType()),
//            new CompStmt(new AssignStmt("a", new ValueExp(new IntValue(1))),
//                    new CompStmt(new VarDeclStmt("b", new IntType()),
//                            new CompStmt(new AssignStmt("b", new ValueExp(new IntValue(1))),
//                                    new PrintStmt(new RelationalExp(new VarExp("a"), "==", new VarExp("b")))))));
//
//    IStmt ex4 = new CompStmt(new VarDeclStmt("v", new IntType()),
//        new CompStmt(new AssignStmt("v", new ValueExp(new IntValue(2))),
//              new PrintStmt(new VarExp("v"))));
//
//    //int a; int b; a=2+3*5; b =a+1; Print(b) is represented as:
//    IStmt ex2 = new CompStmt( new VarDeclStmt("a",new IntType()),
//            new CompStmt(new VarDeclStmt("b",new IntType()),
//                    new CompStmt(new AssignStmt("a", new ArithExp('+',new ValueExp(new IntValue(2)),new
//                            ArithExp('*',new ValueExp(new IntValue(3)), new ValueExp(new IntValue(5))))),
//                            new CompStmt(new AssignStmt("b",new ArithExp('+',new VarExp("a"), new ValueExp(new
//                                    IntValue(1)))), new PrintStmt(new VarExp("b"))))));
//
//    //bool a; int v; a=true;(If a Then v=2 Else v=3);Print(v) is represented as
//    IStmt ex3 = new CompStmt(new VarDeclStmt("a",new BooleanType()),
//            new CompStmt(new VarDeclStmt("v", new IntType()),
//                    new CompStmt(new AssignStmt("a", new ValueExp(new BoolValue(true))),
//                            new CompStmt(new IfStmt(new VarExp("a"),new AssignStmt("v",new ValueExp(new
//                                    IntValue(2))), new AssignStmt("v", new ValueExp(new IntValue(3)))), new PrintStmt(new
//                                    VarExp("v"))))));

//    public int getDisplayOption(){
//        Scanner scanner = new Scanner(System.in);
//        int choice = 0;
//        boolean exit = false;
//        while(!exit){
//            try{
//                System.out.println("Select if you want all the steps or just the result:");
//                System.out.println("1. All");
//                System.out.println("2. Just the result");
//                System.out.print("Enter your choice: ");
//                choice = scanner.nextInt();
//                if (choice >= 1 && choice <= 2) {
//                    break;  // Exit the loop if the input is valid
//                } else {
//                    throw new MyException("Not a valid input, input 1, 2");
//                }
//            } catch (MyException e ){
//                System.out.println(e);
//            }
//            catch (InputMismatchException e){
//                System.out.println("Invalid input. Please enter a number.");
//                scanner.next();
//            }
//        }
//        return choice;
//    }
//    public void menu(){
//        Scanner scanner = new Scanner(System.in);
//        int displayOption = getDisplayOption();
//        int exempleOption;
//        boolean exit = false;
//
//        while (!exit) {
//            System.out.println();
//            System.out.println("Switch Menu:");
//            System.out.println("1. Option 1" + ex1);
//            System.out.println("2. Option 2" + ex2);
//            System.out.println("3. Option 3" + ex3);
//            System.out.println("0. End");
//
//            System.out.print("Enter your choice: ");
//            exempleOption = scanner.nextInt();
//            switch (exempleOption) {
//                case 1:
//                    //System.out.println("You selected Option 1");
//                    System.out.println();
//                    //runExample1(displayOption);
//                    break;
//                case 2:
//                    //System.out.println("You selected Option 2");
//                    System.out.println();
//                    //runExample2(displayOption);
//                    break;
//                case 3:
//                    //System.out.println("You selected Option 3");
//                    System.out.println();
//                    //runExample3(displayOption);
//                    break;
//                case 0:
//                    System.out.println("Exiting the program.");
//                    exit = true;
//                    break;
//                default:
//                    System.out.println("Invalid choice. Please enter a valid option.");
//                    break;
//            }
//        }
//        scanner.close();
//    }
//
//    public static void main(String[] arg){
//        View view =  new View();
//        view.menu();
//    }
//    public void runExample1(int displayOption) {
//        MyIStack<IStmt> stk = new MyStack<IStmt>();
//        MyIDictionary<String, Value> symtbl = new MyDictionary<String,Value>();
//        MyIDictionary<String, BufferedReader> fileTable = new MyDictionary<>();
//        MyIList<Value> out = new MyList<Value>();
//        PrgState crtPrgState = new PrgState(stk,symtbl,out, ex1, fileTable);
//        IRepository repo = new Repository();
//        repo.add(crtPrgState);
//        Controller controller = new Controller(repo);
//        try {
//            controller.allStep(displayOption);
//        }catch(MyException e){
//            System.out.println(e.getMessage());
//        }
//    }
//    public void runExample2(int displayOption) {
//        MyIStack<IStmt> stk = new MyStack<IStmt>();
//        MyIDictionary<String, Value> symtbl = new MyDictionary<String,Value>();
//        MyIDictionary<String, BufferedReader> fileTable = new MyDictionary<>();
//        MyIList<Value> out = new MyList<Value>();
//        PrgState crtPrgState = new PrgState(stk,symtbl,out, ex2,fileTable);
//        IRepository repo = new Repository();
//        repo.add(crtPrgState);
//        Controller controller = new Controller(repo);
//        try {
//            controller.allStep(displayOption);
//        }catch(MyException e){
//            System.out.println(e.getMessage());
//        }
//    }
//    public void runExample3(int displayOption) {
//        MyIStack<IStmt> stk = new MyStack<IStmt>();
//        MyIDictionary<String, Value> symtbl = new MyDictionary<String,Value>();
//        MyIDictionary<String, BufferedReader> fileTable = new MyDictionary<>();
//        MyIList<Value> out = new MyList<Value>();
//        PrgState crtPrgState = new PrgState(stk,symtbl,out, ex3,fileTable);
//        IRepository repo = new Repository();
//        repo.add(crtPrgState);
//        Controller controller = new Controller(repo);
//        try {
//            controller.allStep(displayOption);
//        }catch(MyException e){
//            System.out.println(e.getMessage());
//        }
//    }
//}
