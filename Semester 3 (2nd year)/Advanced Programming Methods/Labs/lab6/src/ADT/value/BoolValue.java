package ADT.value;

import ADT.types.BooleanType;
import ADT.types.Type;

public class BoolValue implements Value{
    Boolean value;
    public BoolValue(Boolean b){
        this.value = b;
    }
    @Override
    public Type getType() {
        return new BooleanType();
    }

    public boolean getValue() {
        return this.value;
    }
    public String toString(){
        return String.valueOf(value);
    }
}
