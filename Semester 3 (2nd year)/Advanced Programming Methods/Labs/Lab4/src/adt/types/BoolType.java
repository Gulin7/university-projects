package adt.types;

import adt.values.BoolValue;
import adt.values.Value;

public class BoolType implements Type {
    @Override
    public boolean equals(Object another){
        return another instanceof BoolType;
    }

    @Override
    public String toString() {
        return "boolean";
    }

    @Override
    public Value defaultValue()
    {
        return new BoolValue(false);
    }
}
