package ADT.types;

import ADT.value.BoolValue;
import ADT.value.Value;

public class BooleanType implements Type{
    @Override
    public boolean equals(Object another){
        return another instanceof BooleanType;
    }
    @Override
    public String toString() {
        return "boolean";
    }
    @Override
    public Value defaultValue() {
        return new BoolValue(false);
    }
}

