package ADT.types;

import ADT.value.StringValue;
import ADT.value.Value;

public class StringType implements Type{
    @Override
    public Value defaultValue() {
        return new StringValue("");
    }
    @Override
    public boolean equals(Object another){
        return another instanceof StringType;
    }
    @Override
    public String toString(){
        return "string";
    }
}
