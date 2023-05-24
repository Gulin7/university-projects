#pragma once
#include <vector>
#include <utility>

typedef int TKey;
typedef int TValue;
typedef std::pair<TKey, TValue> TElem;

class MultiMapIterator;

class MultiMap
{
    friend class MultiMapIterator;
public:
    TElem* table;
    int* next;
    int capacity;
    int firstEmpty;
    int length;
    int TFunction(TKey k);
    /* representation of the MultiMap */

    //constructor

    MultiMap();

    //adds a key value pair to the multimap

    void add(TKey c, TValue v);


    //removes a key value pair from the multimap

    //returns true if the pair was removed (if it was in the multimap) and false otherwise

    bool remove(TKey c, TValue v);


    //returns the vector of values associated to a key. If the key is not in the MultiMap, the vector is empty

    std::vector<TValue> search(TKey c);


    //returns the number of pairs from the multimap

    int size() const;


    //checks whether the multimap is empty

    bool isEmpty() const;

    void rehash();

    void resize();

    int resetFirstEmpty();

    int addIfNotPresent(MultiMap& m);

    //returns an iterator for the multimap

    MultiMapIterator iterator() const;


    //descturctor

    ~MultiMap();

};