package ADT.value;

import ADT.types.IntType;
import ADT.types.Type;

public class IntValue implements Value{
    int val;
    public IntValue(int v){
        val=v;
    }
    public int getValue() {
        return val;
    }

    public String toString() {
        return String.valueOf(val);
    }
    public Type getType() {
        return new IntType();
    }

}