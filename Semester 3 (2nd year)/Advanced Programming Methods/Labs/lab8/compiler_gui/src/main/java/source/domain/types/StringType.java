package source.domain.types;

import source.domain.values.IValue;
import source.domain.values.StringValue;

public class StringType implements Type {
    @Override
    public boolean equals(Object obj) {
        return obj instanceof StringType;
    }

    @Override
    public String toString() {
        return "string";
    }

    @Override
    public IValue defaultValue() {
        return new StringValue("");
    }
}
