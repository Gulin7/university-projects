package ADT.value;

import ADT.types.RefType;
import ADT.types.Type;

public class RefValue implements Value{
    int address;
    Type locationType;
    public RefValue(int address, Type type){
        this.address = address;
        this.locationType = type;
    }
    public int getAddr() {
        return address;
    }
    public void setAddress(int address){
        this.address = address;
    }
    public Type getType() {
        return new RefType(locationType);
    }
    @Override
    public String toString() {
        return "(" + locationType + ", " + address + ")";
    }
}