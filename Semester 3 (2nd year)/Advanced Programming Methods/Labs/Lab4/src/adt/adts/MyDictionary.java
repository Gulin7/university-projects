package adt.adts;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class MyDictionary<Key, Value> implements MyIDictionary<Key, Value>{
    private Map<Key, Value> map;

    public MyDictionary() {
        map = new HashMap<>();
    }

    @Override
    public void put(Key key, Value value) {
        map.put(key, value);
    }

    @Override
    public void remove(Key key)
    {
        map.remove(key);
    }

    @Override
    public boolean isDefined(Key key) {
        return map.get(key) != null;
    }

    @Override
    public Value lookUp(Key key) {
        return map.get(key);
    }

    @Override
    public Set<Key> getKey() {
        return map.keySet();
    }

    @Override
    public void update(Key key, Value v) {
        map.put(key, v);
    }

    @Override
    public String toString() {
        return map.toString();
    }

    public Map<Key, Value> getMap() {
        return map;
    }

    public void setMap(Map<Key, Value> map) {
        this.map = map;
    }
}
