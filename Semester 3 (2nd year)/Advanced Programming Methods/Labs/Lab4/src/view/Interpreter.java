package view;

import adt.*;
import adt.adts.*;
import adt.expressions.ArithmeticExpression;
import adt.expressions.RelationalExpression;
import adt.expressions.ValueExpression;
import adt.expressions.VariableExpression;
import adt.statements.*;
import adt.statements.filesStmts.CloseFileStmt;
import adt.statements.filesStmts.OpenReadFileStmt;
import adt.statements.filesStmts.ReadFileStmt;
import adt.types.BoolType;
import adt.types.IntType;
import adt.types.StringType;
import adt.values.*;
import commands.ExitCommand;
import commands.RunExample;
import controller.Controller;
import repository.Repository;

import textmenu.TextMenu;

public class Interpreter {

    public static void main(String[] args) {
        IStmt example1 = new CompoundStmt(new VariableDeclarationStmt("v", new IntType()),
                new CompoundStmt(new AssignmentStmt("v", new ValueExpression(new IntValue(2))),
                        new PrintStmt(new VariableExpression("v"))));


        IStmt example2 = new CompoundStmt(new VariableDeclarationStmt("a", new IntType()),
                new CompoundStmt(new VariableDeclarationStmt("b", new IntType()),
                        new CompoundStmt(new AssignmentStmt("a",
                                new ArithmeticExpression('+', new ValueExpression(new IntValue(2)),
                                        new ArithmeticExpression('*', new ValueExpression(new IntValue(3)),
                                                new ValueExpression(new IntValue(5))))),
                                new CompoundStmt(new AssignmentStmt("b", new ArithmeticExpression('+',
                                        new VariableExpression("a"), new ValueExpression(new IntValue(1)))),
                                        new PrintStmt(new VariableExpression("b"))))));
        IStmt example3 = new CompoundStmt(new VariableDeclarationStmt("a", new BoolType()),
                new CompoundStmt(new VariableDeclarationStmt("v", new IntType()),
                        new CompoundStmt(new AssignmentStmt("a", new ValueExpression(new BoolValue(true))),
                                new CompoundStmt(new IfStmt(new RelationalExpression(new ValueExpression(new IntValue(5)),
                                        new ValueExpression(new IntValue(5)), "=="),
                                        new AssignmentStmt("v", new ValueExpression(new IntValue(2))),
                                        new AssignmentStmt("v", new ValueExpression(new IntValue(3)))),
                                        new PrintStmt(new VariableExpression("v"))))));

        IStmt example4 = new CompoundStmt(new VariableDeclarationStmt("varf", new StringType()),
                new CompoundStmt(new AssignmentStmt("varf", new ValueExpression(new StringValue
                        ("C:\\Codes\\university-projects\\Semester 3 (2nd year)\\Advanced Pr Methods\\Labs\\Lab4\\Lab4\\test.in"))),
                        new CompoundStmt(new OpenReadFileStmt(new VariableExpression("varf")), new CompoundStmt
                                (new VariableDeclarationStmt("varc", new IntType()), new CompoundStmt
                                        (new ReadFileStmt(new VariableExpression("varf"), "varc"), new CompoundStmt
                                                (new PrintStmt(new VariableExpression("varc")), new CompoundStmt
                                                        (new ReadFileStmt(new VariableExpression("varf"), "varc"),
                                                                new CompoundStmt(new PrintStmt(new VariableExpression("varc")),
                                                                        new CloseFileStmt(new VariableExpression("varf"))))))))));
        ProgramState st1 = new ProgramState(new MyStack<>(), new MyDictionary<>(), new MyList<>(),
                new MyDictionary<>(), example1);
        ProgramState st2 = new ProgramState(new MyStack<>(), new MyDictionary<>(), new MyList<>(),
                new MyDictionary<>(), example2);
        ProgramState st3 = new ProgramState(new MyStack<>(), new MyDictionary<>(), new MyList<>(),
                new MyDictionary<>(), example3);
        ProgramState st4 = new ProgramState(new MyStack<>(), new MyDictionary<>(), new MyList<>(),
                new MyDictionary<>(), example4);

        Repository repo1 = new Repository(st1, "C:\\Codes\\university-projects\\Semester 3 (2nd year)\\Advanced Pr Methods\\Labs\\Lab4\\Lab4\\src\\logFile.txt");
        Repository repo2 = new Repository(st2, "C:\\Codes\\university-projects\\Semester 3 (2nd year)\\Advanced Pr Methods\\Labs\\Lab4\\Lab4\\src\\logFile.txt");
        Repository repo3 = new Repository(st3, "C:\\Codes\\university-projects\\Semester 3 (2nd year)\\Advanced Pr Methods\\Labs\\Lab4\\Lab4\\src\\logFile.txt");
        Repository repo4 = new Repository(st4, "C:\\Codes\\university-projects\\Semester 3 (2nd year)\\Advanced Pr Methods\\Labs\\Lab4\\Lab4\\src\\logFile.txt");

        Controller c1 = new Controller(repo1);
        Controller c2 = new Controller(repo2);
        Controller c3 = new Controller(repo3);
        Controller c4 = new Controller(repo4);


        TextMenu menu = new TextMenu();
        menu.addCommand(new ExitCommand("0", "exit"));
        menu.addCommand(new RunExample("1", example1.toString(), c1));
        menu.addCommand(new RunExample("2", example2.toString(), c2));
        menu.addCommand(new RunExample("3", example3.toString(), c3));
        menu.addCommand(new RunExample("4", example4.toString(), c4));

        menu.show();
    }
}
