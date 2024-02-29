package ADT.types;

import ADT.value.IntValue;
import ADT.value.Value;

public class IntType implements Type{
    @Override
    public boolean equals(Object another){
        return another instanceof IntType;
    }
    @Override
    public String toString() {
        return "int";
    }
    @Override
    public Value defaultValue() {
        return new IntValue(0);
    }
}
