package source.domain.types;

import source.domain.values.IValue;
import source.domain.values.IntValue;

public class IntType implements Type {
    @Override
    public boolean equals(Object obj) {
        return obj instanceof IntType;
    }

    @Override
    public String toString() {
        return "int";
    }

    @Override
    public IValue defaultValue() {
        return new IntValue(0);
    }
}
