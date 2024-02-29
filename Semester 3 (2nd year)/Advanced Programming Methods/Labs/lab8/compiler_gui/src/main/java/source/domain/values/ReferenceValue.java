package source.domain.values;

import source.domain.types.ReferenceType;
import source.domain.types.Type;

public class ReferenceValue implements IValue {
    private final Type referenceType;
    private int heapAddress;

    public ReferenceValue(int heapAddress, Type referenceType)
    {
        this.heapAddress = heapAddress;
        this.referenceType = referenceType;
    }

    public int getHeapAddress()
    {
        return this.heapAddress;
    }

    public void setHeapAddress(int newAddress)
    {
        this.heapAddress = newAddress;
    }

    @Override
    public Type getType() {
        return new ReferenceType(referenceType);
    }

    @Override
    public String toString() {
        return "(" + this.heapAddress + ", " + this.referenceType.toString() + ")";
    }
}
