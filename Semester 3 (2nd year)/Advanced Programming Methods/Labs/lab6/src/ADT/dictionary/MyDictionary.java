package ADT.dictionary;

import ADT.types.Type;

import java.util.HashMap;
import java.util.Map;

public class MyDictionary<K, V> implements MyIDictionary<K, V>{
    private Map<K, V> map;

    public MyDictionary(){
        map = new HashMap<K, V>();
    }
    @Override
    public void put(K k, V v) {
        map.put(k, v);
    }
    @Override
    public boolean isDefined(K k) {
        return map.get(k) != null;
    }
    @Override
    public V lookup(K k) {
        return  map.get(k);
    }

    @Override
    public void update(K id, V val) {
        this.map.put(id, val);
    }

    @Override
    public void delete(K id) {
        map.remove(id);
    }

    public String toString(){
        return  "My dictionary{" + "map="+map+'}';
    }
    public Map<K, V> getMap(){
        return map;
    }

    @Override
    public MyIDictionary<String, Type> clone() {
        MyIDictionary<K,V> copy = new MyDictionary<>();
        for (K k : map.keySet()) {
            copy.update(k, map.get(k));
        }
        return (MyIDictionary<String, Type>) copy;
    }


    public void setMap(Map<K, V> map){
        this.map=map;
    }


}