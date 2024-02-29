package adt.values;

import adt.types.ReferenceType;
import adt.types.Type;

public class ReferenceValue implements Value {
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
    public Object getValue() {
        return null;
    }

    @Override
    public String toString() {
        return "(" + this.heapAddress + ", " + this.referenceType.toString() + ")";
    }
}