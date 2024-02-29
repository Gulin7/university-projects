package source.domain.statements;

import source.domain.ProgramState;
import source.domain.adts.MyIDictionary;
import source.domain.types.Type;
import source.exceptions.InterpreterException;
import source.domain.values.IValue;

public class VariableDeclarationStatement implements IStatement {
    private final String variableId;
    private final Type variableType;

    public VariableDeclarationStatement(String variableId, Type variableType)
    {
        this.variableId = variableId;
        this.variableType = variableType;
    }

    /**
     * Executes a VariableDeclarationStatement, adding a new variable to the symbol table with the specified type
     * and initializing it with the default value of the type.
     *
     * @param currentState The current program state.
     * @return The updated program state after executing the variable declaration statement.
     * @throws InterpreterException If the variable is already defined.
     */
    @Override
    public ProgramState execute(ProgramState currentState) throws InterpreterException {
        MyIDictionary<String, IValue> symbolTable = currentState.getSymbolTable();

        String errorThreadIdentifier = "Thread: " + currentState.getId() + " - ";

        // Check if the variable is already defined
        if (symbolTable.isDefined(variableId))
            throw new InterpreterException(errorThreadIdentifier +
                    "Variable already defined!");

        // Put the new variable in the symbol table and initialize it with the default value of the type
        symbolTable.put(variableId, variableType.defaultValue());

        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeTable) throws InterpreterException {
        typeTable.put(variableId, variableType);

        return typeTable;
    }

    @Override
    public String toString() {
        return variableType + " " + variableId;
    }
}
