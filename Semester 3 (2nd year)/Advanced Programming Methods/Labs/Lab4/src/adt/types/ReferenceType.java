package adt.types;

import adt.values.Value;
import adt.values.ReferenceValue;

public class ReferenceType implements Type {
    private final Type innerType;

    public ReferenceType(Type innerType)
    {
        this.innerType = innerType;
    }

    public Type getInnerType()
    {
        return this.innerType;
    }

    @Override
    public Value defaultValue() {
        return new ReferenceValue(0, innerType);
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof ReferenceType another)
            return this.innerType.equals(another.getInnerType());

        return false;
    }

    @Override
    public String toString() {
        return "Ref(" + innerType.toString() + ")";
    }
}