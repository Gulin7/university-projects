package source.domain.values;

import source.domain.types.BoolType;
import source.domain.types.Type;

public class BoolValue implements IValue {
    private final boolean value;

    public BoolValue(boolean value)
    {
        this.value = value;
    }

    public boolean getValue()
    {
        return this.value;
    }

    @Override
    public boolean equals(Object obj) {
        if (! (obj instanceof BoolValue))
            return false;

        BoolValue objValue = (BoolValue) obj;
        return this.getValue() == objValue.getValue();
    }

    @Override
    public Type getType() {
        return new BoolType();
    }

    @Override
    public String toString() {
        return String.valueOf(value);
    }
}
