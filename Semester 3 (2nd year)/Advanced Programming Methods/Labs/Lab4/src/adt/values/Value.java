package adt.values;

import adt.types.Type;

public interface Value {
    Type getType();

    Object getValue();
}
