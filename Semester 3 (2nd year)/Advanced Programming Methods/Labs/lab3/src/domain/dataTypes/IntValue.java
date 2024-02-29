package domain.dataTypes;

public class IntValue implements IValue {
    private final int value; // it's int value

    public IntValue(int value) {
        this.value = value;
    } // constructor

    public int getValue() {
        return this.value; // get's the value
    }

    @Override
    public String toString() { return Integer.toString(this.value);}

    @Override
    public IType getType() {
        return new IntType(); // as type it returns IntType
    }
}
