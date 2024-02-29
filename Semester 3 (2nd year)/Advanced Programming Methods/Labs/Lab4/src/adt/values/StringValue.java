package adt.values;

import adt.types.StringType;
import adt.types.Type;

public class StringValue implements Value{
    String value;

    public StringValue(String string)
    {
        value = string;
    }

    @Override
    public String getValue()
    {
        return value;
    }

    @Override
    public String toString()
    {
        return value;
    }

    @Override
    public Type getType()
    {
        return new StringType();
    }
}
