#include "MultiMap.h"
#include "MultiMapIterator.h"
#include <exception>
#include <iostream>

using namespace std;


MultiMap::MultiMap() {
    this->cap = 15;
    this->currSize = 0;
    this->elems = new Keys[this->cap];
    this->next = new int[this->cap];
    this->head = -1;

    for (int i = 0; i < cap - 1; i++)
        this->next[i] = i + 1;

    this->next[this->cap - 1] = -1;
    this->firstFree = 0;

}


void MultiMap::add(TKey c, TValue v) {
    if (this->firstFree == -1)
        this->resize();

    // if SLLA is empty, add to front
    if (this->head == -1) {
        this->head = 0;
        this->elems[head] = keys(c); // create new key c
        this->elems[head].add(v);
        this->firstFree = this->next[0];
        this->next[head] = -1;
        this->currSize++;

        return;

    }

    // check if key already exists
    int current = this->head;
    int prev = -1;

    while (current != -1) {
        if (this->elems[current].key == c) {
            // add to already existing key
            this->elems[current].add(v);
            this->currSize++;
            return;

        }

        prev = current;
        current = this->next[current];

    }

    // key doesn't exist, create a new one at the end
    int oldFirstFree = this->firstFree;
    this->firstFree = this->next[oldFirstFree];
    this->elems[oldFirstFree] = keys(c);
    this->elems[oldFirstFree].add(v);
    this->next[oldFirstFree] = current;
    this->next[prev] = oldFirstFree;

    this->currSize++;

}


bool MultiMap::remove(TKey c, TValue v) {
    int current = head;
    int previous = -1;

    // find the correct key
    while (current != -1 && this->elems[current].key != c) {
        previous = current;
        current = this->next[current];

    }

    // can't find key
    if (current == -1)
        return false;

    // found key
    // try to remove value from key
    if (!this->elems[current].remove(v))
        return false;

    // if the key no longer has any values, remove key completely
    if (this->elems[current].currSize == 0) {
        if (previous != -1)
            // key is in the middle of the list
            this->next[previous] = this->next[current];

        else
            // key is at the beginning
            this->head = this->next[current];

        this->next[current] = this->firstFree;
        this->firstFree = current;

        delete[] this->elems[current].values;
        delete[] this->elems[current].next;

    }

    this->currSize--;
    return true;

}


vector<TValue> MultiMap::search(TKey c) const {
    int current = this->head;

    while (current != -1 && this->elems[current].key != c)
        current = this->next[current];

    if (current == -1)
        return vector<TValue>();

    return this->elems[current].getElems();
}


int MultiMap::size() const {
    return this->currSize;

}


bool MultiMap::isEmpty() const {
    return this->currSize == 0;

}

MultiMapIterator MultiMap::iterator() const {
    return MultiMapIterator(*this);
}


MultiMap::~MultiMap() {
    delete[] this->elems;
    delete[] this->next;

}

MultiMap::Keys MultiMap::keys(TKey k) {
    Keys keyList;
    keyList.key = k;
    keyList.cap = 15;
    keyList.currSize = 0;

    keyList.head = -1;
    keyList.values = new TValue[this->cap];
    keyList.next = new int[this->cap];

    for (int i = 0; i < cap - 1; i++)
        keyList.next[i] = i + 1;

    keyList.next[keyList.cap - 1] = -1;
    keyList.firstFree = 0;

    return keyList;

}

void MultiMap::Keys::add(TValue e) {
    if (firstFree == -1)
        resize();

    // if SLLA is empty, add to front
    if (head == -1) {
        head = 0;
        values[head] = e;
        firstFree = next[firstFree];
        next[head] = -1;
        currSize++;

        return;

    }

    // else add to the first free position and move firstFree to next[firstFree]
    int oldFirstFree = firstFree;
    firstFree = next[firstFree];
    values[oldFirstFree] = e;
    next[oldFirstFree] = head;
    head = oldFirstFree;
    currSize++;

}

bool MultiMap::Keys::remove(TValue e) {
    int current = head;
    int previous = -1;

    // find the correct value
    while (current != -1 && values[current] != e) {
        previous = current;
        current = next[current];

    }

    // can't find value
    if (current == -1)
        return false;

    // value found is the first one
    if (previous == -1) {
        int oldFirstFree = firstFree;
        firstFree = head;

        head = next[head];
        next[firstFree] = oldFirstFree;

        currSize--;
        return true;

    }

    // remove value in the middle of the list
    int oldFirstFree = firstFree;
    firstFree = current;
    next[previous] = next[current];
    next[current] = next[oldFirstFree];

    currSize--;
    return true;

}

void MultiMap::Keys::resize() {
    TValue* newValues = new TValue[cap * 2];
    int* newNext = new int[cap * 2];

    for (int i = 0; i < cap; i++) {
        newValues[i] = values[i];
        newNext[i] = next[i];

    }

    for (int i = cap; i < cap * 2; i++)
        newNext[i] = i + 1;

    newNext[cap * 2 - 1] = -1;
    firstFree = cap;
    cap *= 2;

    delete[] values;
    delete[] next;

    values = newValues;
    next = newNext;

}

vector<TValue> MultiMap::Keys::getElems() const {
    vector<TValue> valuesVector;
    int i = head;
    while (i != -1) {
        valuesVector.push_back(values[i]);
        i = next[i];

    }

    return valuesVector;

}

void MultiMap::resize() {
    Keys* newKeys = new Keys[this->cap * 2];
    int* newNext = new int[this->cap * 2];

    for (int i = 0; i < this->cap; i++) {
        newKeys[i] = this->elems[i];
        newNext[i] = this->next[i];

    }

    for (int i = this->cap; i < this->cap * 2; i++)
        newNext[i] = i + 1;

    newNext[this->cap * 2 - 1] = -1;
    this->firstFree = this->cap;
    this->cap *= 2;

    delete[] this->elems;
    delete[] this->next;

    this->elems = newKeys;
    this->next = newNext;

}
