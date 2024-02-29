package ADT.value;

import ADT.types.StringType;
import ADT.types.Type;

public class StringValue implements Value{
    String val;
    public StringValue(String v){
        this.val=v;
    }
    public String getVal(){
        return this.val;
    }
    public String toString() {
        return val;
    }
    @Override
    public Type getType() {
        return new StringType();
    }
}
