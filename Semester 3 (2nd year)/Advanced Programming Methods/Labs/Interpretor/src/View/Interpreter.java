package View;
import ADT.PrgState;
import ADT.dictionary.MyDictionary;
import ADT.expresion.*;
import ADT.heap.MyHeap;
import ADT.list.MyList;
import ADT.stack.MyStack;
import ADT.statement.*;
import ADT.types.BooleanType;
import ADT.types.IntType;
import ADT.types.RefType;
import ADT.types.StringType;
import ADT.value.BoolValue;
import ADT.value.IntValue;
import ADT.value.StringValue;
import Controller.Controller;
import View.TextMenu;
import repository.IRepository;
import repository.Repository;

public class Interpreter {
    public static void main(String[] args) {
        IStmt ex0 = new CompStmt(new VarDeclStmt("varf", new StringType()),
                new CompStmt(new AssignStmt("varf", new ValueExp(new StringValue("C:\\Codes\\university-projects\\Semester 3 (2nd year)\\Advanced Pr Methods\\Labs\\A2-interpretor\\A4\\src\\logfile.txt"))), new PrintStmt(new VarExp("varf"))));

        IStmt ex1 = new CompStmt(new VarDeclStmt("varf", new StringType()),
                new CompStmt(new AssignStmt("varf", new ValueExp(new StringValue("C:\\Codes\\university-projects\\Semester 3 (2nd year)\\Advanced Pr Methods\\Labs\\A2-interpretor\\A4\\src\\logfile.txt"))),
                        new CompStmt(new OpenRFileStmt(new VarExp("varf")),
                                new CompStmt(new VarDeclStmt("varc", new IntType()),
                                        new CompStmt(new ReadFileStmt(new VarExp("varf"), "varc"),
                                                new CompStmt(new PrintStmt(new VarExp("varc")),
                                                        new CloseRFileStmt(new VarExp("varf"))))))));

        IStmt ex4 = new CompStmt(new VarDeclStmt("v", new IntType()),
                new CompStmt(new AssignStmt("v", new ValueExp(new IntValue(2))),
                        new PrintStmt(new VarExp("v"))));

        //int a; int b; a=2+3*5; b =a+1; Print(b) is represented as:
        IStmt ex2 = new CompStmt(new VarDeclStmt("a", new IntType()),
                new CompStmt(new VarDeclStmt("b", new IntType()),
                        new CompStmt(new AssignStmt("a", new ArithExp('+', new ValueExp(new IntValue(2)), new
                                ArithExp('*', new ValueExp(new IntValue(3)), new ValueExp(new IntValue(5))))),
                                new CompStmt(new AssignStmt("b", new ArithExp('+', new VarExp("a"), new ValueExp(new
                                        IntValue(1)))), new PrintStmt(new VarExp("b"))))));

        //bool a; int v; a=true;(If a Then v=2 Else v=3);Print(v) is represented as
        IStmt ex3 = new CompStmt(new VarDeclStmt("a", new BooleanType()),
                new CompStmt(new VarDeclStmt("v", new IntType()),
                        new CompStmt(new AssignStmt("a", new ValueExp(new BoolValue(true))),
                                new CompStmt(new IfStmt(new VarExp("a"), new AssignStmt("v", new ValueExp(new
                                        IntValue(2))), new AssignStmt("v", new ValueExp(new IntValue(3)))), new PrintStmt(new
                                        VarExp("v"))))));
        IStmt ex5 = new CompStmt(
                new VarDeclStmt ("v",new IntType()),
                new CompStmt(
                        new AssignStmt("v",new ValueExp(new IntValue(10))),
                        new WhileStmt(
                                new RelationalExp(new VarExp("v"),">",new ValueExp(new IntValue(0))),
                                new CompStmt(new PrintStmt(new VarExp("v")),
                                        new AssignStmt( "v",new ArithExp('-',new VarExp("v"),new ValueExp(new IntValue(1))))
                                )
                        )));

        IStmt ex6 = new CompStmt(
                new VarDeclStmt("v",new RefType(new IntType())),
                new CompStmt(
                        new NewStmt("v",new ValueExp(new IntValue(20))),
                        new CompStmt(
                                new PrintStmt(new ReadHeapExp(new VarExp("v"))), new CompStmt(
                                new VarDeclStmt("a",new RefType(new RefType(new  IntType()))), new CompStmt(
                                new NewStmt("a",new VarExp("v")),new CompStmt(
                                new NewStmt("v",new ValueExp(new IntValue(20))),
                                new PrintStmt(new ArithExp('+' ,new ReadHeapExp(new ReadHeapExp( new VarExp("a"))),new ValueExp(new IntValue(5))))))))));
        IStmt ex7 =  new CompStmt(
                new VarDeclStmt("v",new RefType(new IntType())),
                new CompStmt(
                        new NewStmt("v",new ValueExp(new IntValue(20))),
                        new CompStmt(
                                new PrintStmt(new ReadHeapExp(new VarExp("v"))), new CompStmt(
                                new VarDeclStmt("a",new RefType(new RefType(new  IntType()))), new CompStmt(
                                new NewStmt("a",new VarExp("v")),new CompStmt(
                                new HeapWriteStmt("v",new ValueExp(new IntValue(30))),
                                new PrintStmt(new ArithExp('+' ,new ReadHeapExp(new ReadHeapExp( new VarExp("a"))),new ValueExp(new IntValue(5))))))))));

        IStmt ex8 = new CompStmt(
                new VarDeclStmt("v",new RefType(new IntType())),
                new CompStmt(
                        new NewStmt("v",new ValueExp(new IntValue(21))),
                                new CompStmt(
                                new VarDeclStmt("a",new RefType(new RefType(new  IntType()))), new CompStmt(
                                new NewStmt("a",new VarExp("v")),
                                new CompStmt(new NewStmt("v",new ValueExp(new IntValue(31))),
                                        new PrintStmt(new ReadHeapExp(new ReadHeapExp( new VarExp("a")))))))));

        //IStmt ex8 = new CompStmt(
          //      new VarDeclStmt("v", new RefType(new IntType())),
            //    new CompStmt(new NewStmt("v", new ValueExp(new IntValue(20))),
              ///               new CompStmt(new VarDeclStmt("a", new IntType())),
                 //           new CompStmt(new NewStmt("a",new VarExp("v")),
                   //                 new NewStmt("v",new ValueExp(new IntValue(20))),
                     //               new PrintStmt(new ReadHeapExp(new ReadHeapExp(new VarExp("a"))))))
        //)
        PrgState prg1 = new PrgState(new MyStack(), new MyDictionary(), new MyList(), ex1, new MyDictionary(), new MyHeap<>());
        IRepository repo1 = new Repository(prg1, "log1.txt");
        Controller ctr1 = new Controller(repo1);

        PrgState prg2 = new PrgState(new MyStack(), new MyDictionary(), new MyList(), ex2, new MyDictionary(), new MyHeap<>());
        IRepository repo2 = new Repository(prg2, "log2.txt");
        Controller ctr2 = new Controller(repo2);

        PrgState prg3 = new PrgState(new MyStack(), new MyDictionary<>(), new MyList(), ex3, new MyDictionary(), new MyHeap<>());
        IRepository repo3 = new Repository(prg3, "log3.txt");
        Controller ctr3 = new Controller(repo3);

        PrgState prg4 = new PrgState(new MyStack<>(), new MyDictionary<>(), new MyList<>(), ex4, new MyDictionary<>(), new MyHeap<>());
        IRepository repo4 = new Repository(prg4, "log4.txt");
        Controller ctr4 = new Controller(repo4);

        PrgState prg5 = new PrgState(new MyStack<>(), new MyDictionary<>(), new MyList<>(), ex5, new MyDictionary<>(), new MyHeap<>());
        IRepository repo5 = new Repository(prg5, "log5.txt");
        Controller ctr5 = new Controller(repo5);

        PrgState prg6 = new PrgState(new MyStack<>(), new MyDictionary<>(), new MyList<>(), ex6, new MyDictionary<>(), new MyHeap<>());
        IRepository repo6 = new Repository(prg6, "log6.txt");
        Controller ctr6 = new Controller(repo6);

        PrgState prg7 = new PrgState(new MyStack<>(), new MyDictionary<>(), new MyList<>(), ex6, new MyDictionary<>(), new MyHeap<>());
        IRepository repo7 = new Repository(prg7, "log7.txt");
        Controller ctr7 = new Controller(repo7);

        PrgState prg8 = new PrgState(new MyStack<>(), new MyDictionary<>(), new MyList<>(), ex8, new MyDictionary<>(), new MyHeap<>());
        IRepository repo8 = new Repository(prg8, "log8.txt");
        Controller ctr8 = new Controller(repo8);

        TextMenu menu = new TextMenu();
        menu.addCommand(new ExitCommand("0", "exit"));
        menu.addCommand(new RunExample("1", ex1.toString(), ctr1));
        menu.addCommand(new RunExample("2", ex2.toString(), ctr2));
        menu.addCommand(new RunExample("3", ex3.toString(), ctr3));
        menu.addCommand(new RunExample("4", ex4.toString(), ctr4));
        menu.addCommand(new RunExample("5", ex5.toString(), ctr5));
        menu.addCommand(new RunExample("6", ex6.toString(), ctr6));
        menu.addCommand(new RunExample("7", ex7.toString(), ctr7));
        menu.addCommand(new RunExample("8", ex8.toString(), ctr8));

        menu.show();
    }

}