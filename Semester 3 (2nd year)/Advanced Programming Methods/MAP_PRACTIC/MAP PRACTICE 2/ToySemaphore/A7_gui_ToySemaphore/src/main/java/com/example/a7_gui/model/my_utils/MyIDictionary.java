package com.example.a7_gui.model.my_utils;

import com.example.a7_gui.exceptions.ADTException;

import java.util.Collection;
import java.util.Map;
import java.util.Set;

public interface MyIDictionary<T1,T2> {
    boolean isDefined(T1 key);
    void put(T1 key, T2 value);
    T2 lookUp(T1 key) throws ADTException;
    Collection<T2> values();
    void remove(T1 key) throws ADTException;
    Set<T1> keySet();
    Map<T1, T2> getContent();
    MyIDictionary<T1, T2> deepCopy() throws ADTException;
}