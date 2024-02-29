package ADT.heap;

import java.util.HashMap;
import java.util.Map;

public class MyHeap<V> implements MyIHeap<V>{
    private Map<Integer,V> map;
    private int freeIndex = 1;

    public void incrementLastFreeIndex(){
        this.freeIndex++;
    }
    public int getFreeIndex(){
        return freeIndex;
    }
    public MyHeap(){
        map = new HashMap<Integer, V>();
    }
    @Override
    public void put(V v) {
        int index = this.freeIndex;
        incrementLastFreeIndex();
        map.put(index, v);
    }

    @Override
    public boolean isDefined(int k) {
        return map.get(k) != null;
    }
    @Override
    public V lookup(int k) {
        return  map.get(k);
    }
    @Override
    public void update(int id, V val) {
        this.map.put(id, val);
    }
    @Override
    public void delete(int id) {
        map.remove(id);
    }
    public String toString(){
        return  "My heap{" + "map="+map+'}';
    }
    public Map<Integer, V> getContent(){
        return map;
    }
    public void setContent(Map<Integer, V> map){
        this.map=map;
    }
}
