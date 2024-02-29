package domain.dataTypes;

public class StringValue implements IValue {
    private final String value;

    public StringValue(String value) {
        this.value = value;
    }

    public String getValue() {
        return this.value;
    }

    @Override
    public boolean equals(Object obj) {
        if (!(obj instanceof StringValue))
            return false;

        StringValue objValue = (StringValue) obj;
        return this.getValue().equals(objValue.getValue());
    }

    @Override
    public IType getType() {
        return new StringType();
    }

    @Override
    public String toString() {
        return value;
    }
}
