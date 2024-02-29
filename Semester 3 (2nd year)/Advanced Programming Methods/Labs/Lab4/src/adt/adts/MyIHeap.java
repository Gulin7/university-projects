package adt.adts;

import adt.values.Value;

import java.util.Map;

public interface MyIHeap {
    int getCurrentAddress();
    int allocate(Value valueToAllocate);
    Map<Integer, Value> getContent();
    Value getValueAtAddress(int addressToLook);
    void updateAddress(Integer addressToUpdate, Value newValue);
    boolean isDefined(Integer addressToLook);
    void setContent(Map<Integer, Value> newHeapValues);
}