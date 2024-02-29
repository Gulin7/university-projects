package ui;

import controller.Controller;
import exceptions.*;
import domain.*;
import domain.expressions.*;
import domain.statements.*;
import domain.dataTypes.*;
import domain.utils.*;

import java.util.Scanner;

public class Ui {
    private final Controller controller;
    private final Scanner consoleScanner;
    private boolean displayFlag;

    public Ui(Controller ctrl) {
        controller = ctrl;
        consoleScanner = new Scanner(System.in);
    }

    //TODO add the examples from teams

    public void example1() {
        IStatement firstProgram = new CompoundStatement(
                new VariableDeclarationStatement("v", new BoolType()),
                new CompoundStatement(
                        new AssignStatement("v", new ValueExpression(new BoolValue(true))),
                        new CompoundStatement(
                                new VariableDeclarationStatement("a", new IntType()),
                                new NOPStatement()))
        );

        ProgramState program = new ProgramState(new MyStack<>(), new MyDictionary<>(), new MyList<>(), firstProgram);

        controller.addProgram(program);
    }

    public void example2() {
        IStatement secondProgram = new CompoundStatement
                (
                        new VariableDeclarationStatement("a", new IntType()),
                        new CompoundStatement
                                (
                                        new VariableDeclarationStatement("b", new IntType()),
                                        new CompoundStatement
                                                (
                                                        new AssignStatement("a",
                                                                new ArithmeticExpression('+',
                                                                        new ValueExpression(new IntValue(2)),
                                                                        new ArithmeticExpression('*',
                                                                                new ValueExpression(new IntValue(3)),
                                                                                new ValueExpression(new IntValue(5)))
                                                                )
                                                        ),
                                                        new CompoundStatement(
                                                                new AssignStatement("b",
                                                                        new ArithmeticExpression('+',
                                                                                new VariableExpression("a"),
                                                                                new ValueExpression(new IntValue(1))
                                                                        )
                                                                ),
                                                                new PrintStatement(new VariableExpression("b"))
                                                        )
                                                )
                                )
                );

        ProgramState program = new ProgramState(new MyStack<>(), new MyDictionary<>(), new MyList<>(), secondProgram);

        controller.addProgram(program);
    }

    public void example3() {
        IStatement thirdProgram =
                new CompoundStatement(
                        new VariableDeclarationStatement("a", new BoolType()),
                        new CompoundStatement(
                                new VariableDeclarationStatement("v", new IntType()),
                                new CompoundStatement(
                                        new AssignStatement("a", new ValueExpression(new BoolValue(true))),
                                        new CompoundStatement(
                                                new IfStatement(
                                                        new VariableExpression("a"),
                                                        new AssignStatement("v", new ValueExpression(new IntValue(2))),
                                                        new AssignStatement("v", new ValueExpression(new IntValue(3)))
                                                ),
                                                new PrintStatement(
                                                        new VariableExpression("v")
                                                )
                                        )
                                )
                        )
                );

        ProgramState program = new ProgramState(new MyStack<>(), new MyDictionary<>(), new MyList<>(), thirdProgram);

        controller.addProgram(program);
    }

    //int a; int b;
    // a = 5+2; b = a + 5*5;
//    public void ex4(){
//        IStatement example = new CompoundStatement(
//                new VariableDeclarationStatement("a", new IntType()),
//                new CompoundStatement(
//                        new VariableDeclarationStatement("b", new IntType()),
//                        new CompoundStatement(
//                                new AssignStatement("a",
//                                        new ArithmeticExpression('+'
//                                                new ValueExpression(new IntValue(2)),
//                                                new ValueExpression(new IntValue(5)))),
//                                new CompoundStatement()
//                        )...
//                )
//        )
//    }

    private void runProgram() throws ExpressionException, StatementException, StackException {
        ProgramState program = controller.getCurrentProgram();

        if (!displayFlag) {
            controller.executeAllStatements();
            System.out.println(program);
            return;
        }

        System.out.println(program);
        while (!controller.isEmpty()) {
            controller.executeOneStatement(program);
            System.out.println(program);
        }
    }


    public void runUi() {
        String option;

        while (true) {
            try {
                System.out.println("1-> enable display flag; 0 else");
                option = consoleScanner.nextLine();

                displayFlag = option.equals("1");


                System.out.println("1 -> 1st example");
                System.out.println("2 -> 2nd example");
                System.out.println("3 -> 3rd example");
                System.out.println("4 -> exit");

                option = consoleScanner.nextLine();

                switch (option) {
                    case "1":
                        this.example1();
                        break;

                    case "2":
                        this.example2();
                        break;

                    case "3":
                        this.example3();
                        break;

                    case "4":
                        return;

                    default:
                        System.out.println("Please choose a valid option!");
                }

                this.runProgram();
            } catch (ExpressionException | StatementException | StackException e) {
                System.out.println(e.getMessage());
            }
        }
    }
}
