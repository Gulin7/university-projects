package adt.values;

import adt.types.IntType;
import adt.types.Type;

public class IntValue implements Value{
    int val;
    public IntValue(int v){
        val = v;
    }

    @Override
    public Object getValue(){
        return val;
    }

    @Override
    public String toString() {
        return Integer.toString(val);
    }

    @Override
    public Type getType() {
        return new IntType();
    }

}
