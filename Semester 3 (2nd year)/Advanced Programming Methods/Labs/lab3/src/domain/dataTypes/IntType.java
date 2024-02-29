package domain.dataTypes;

public class IntType implements IType {
    @Override
    public boolean equals(Object obj) { return obj instanceof IntType; }

    @Override
    public String toString() { return "int"; } // returns as type: int
}
