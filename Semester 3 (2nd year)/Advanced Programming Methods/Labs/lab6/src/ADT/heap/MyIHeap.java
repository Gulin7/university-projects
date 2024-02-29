package ADT.heap;
import java.util.Map;

public interface MyIHeap<V>  {
    void put(V v);
    boolean isDefined(int k);
    V lookup(int k);
    String toString();
    void update(int id, V val);
    void delete(int id);
    Map<Integer, V> getContent();
    void setContent(Map<Integer, V> map);

    int getFreeIndex();
}
