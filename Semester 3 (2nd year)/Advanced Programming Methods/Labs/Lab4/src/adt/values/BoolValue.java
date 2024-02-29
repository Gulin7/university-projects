package adt.values;

import adt.types.BoolType;
import adt.types.Type;

public class BoolValue implements Value{
    Boolean val;
    public BoolValue(boolean v){
        val = v;
    }

    public Object getValue(){
        return val;
    }

    @Override
    public String toString() {
        return Boolean.toString(val);
    }

    @Override
    public Type getType() {
        return new BoolType();
    }

}
