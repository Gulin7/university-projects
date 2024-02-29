package adt.adts;

import java.util.Set;

public interface MyIDictionary<Key, Value> {
    void put(Key key, Value v);

    void remove(Key key);

    boolean isDefined(Key key);

    Value lookUp(Key key);

    Set<Key> getKey();

    void update(Key key, Value v);
}
