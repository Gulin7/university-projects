package domain.utils;

import java.util.Set;

public interface MyIDictionary<TKey, TValue> {
    TValue getValue(TKey keyToSearch);

    void add(TKey newKey, TValue newValue);

    boolean isDefined(TKey keyToSearch);

    Set<TKey> getKeySet();
    boolean exists(TKey keyToSearch);
}
