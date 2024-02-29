package domain.utils;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class MyDictionary<TKey, TValue> implements MyIDictionary<TKey, TValue> {

    private final Map<TKey, TValue> dictionary;

    public MyDictionary() {
        this.dictionary = new HashMap<TKey, TValue>();
    }

    @Override
    public TValue getValue(TKey keyToSearch) {
        return this.dictionary.get(keyToSearch);
    }

    @Override
    public boolean isDefined(TKey keyToSearch) {
        return dictionary.containsKey(keyToSearch);
    }

    @Override
    public Set<TKey> getKeySet() {
        return this.dictionary.keySet();
    }

    @Override
    public void add(TKey newKey, TValue newValue) {
        this.dictionary.put(newKey, newValue);
    }

    @Override
    public boolean exists(TKey keyToSearch) {
        return this.dictionary.containsKey(keyToSearch);
    }

    @Override
    public String toString() {
        return "MyDictionary{ dictionary= " + dictionary + " }";
    }
}
