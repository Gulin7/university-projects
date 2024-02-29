package com.example.a7_gui.model.values;


import com.example.a7_gui.model.program_types.StringType;
import com.example.a7_gui.model.program_types.Type;

public class StringValue implements Value{
    private final String value;

    public StringValue(String value) {
        this.value = value;
    }
    @Override
    public Type getType() {
        return new StringType();
    }

    @Override
    public boolean equals(Object anotherValue) {
        if (!(anotherValue instanceof StringValue))
            return false;
        StringValue castValue = (StringValue) anotherValue;
        return this.value.equals(castValue.value);
    }

    @Override
    public Value deepCopy() {
        return new StringValue(value);
    }

    public String getValue() {
        return this.value;
    }

    @Override
    public String toString() {
        return "\"" + this.value + "\"";
    }
}