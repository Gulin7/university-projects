package ADT.dictionary;

import java.util.Map;

public interface MyIDictionary<K, V> {
    void put(K k, V v);
    boolean isDefined(K k);
    V lookup(K k);
    String toString();
    void update(K id, V val);
    void delete(K id);
    Map<K, V> getMap();

}
