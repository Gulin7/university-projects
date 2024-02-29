package adt.types;

import adt.values.StringValue;
import adt.values.Value;


public class StringType implements Type{
    @Override
    public boolean equals(Object string)
    {
        return string instanceof StringType;
    }

    @Override
    public String toString()
    {
        return "string";
    }

    @Override
    public Value defaultValue()
    {
        return new StringValue("");
    }
}
