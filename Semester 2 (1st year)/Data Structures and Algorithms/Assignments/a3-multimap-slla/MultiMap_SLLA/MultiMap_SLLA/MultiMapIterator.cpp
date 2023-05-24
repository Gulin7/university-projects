#include "MultiMapIterator.h"
#include "MultiMap.h"


MultiMapIterator::MultiMapIterator(const MultiMap& c) : map(c) {
    this->head = this->map.head;

    if (this->head != -1)
        this->keysHead = this->map.elems[this->head].head;

    current = 0;

}

TElem MultiMapIterator::getCurrent() const {
    if (!valid())
        throw exception();

    return { this->map.elems[this->head].key, this->map.elems[this->head].values[this->keysHead] };

}

bool MultiMapIterator::valid() const {
    return this->head != -1 && this->map.size() >= this->current;

}

void MultiMapIterator::next() {
    if (!valid())
        throw exception();
    if (this->keysHead != -1 && this->map.elems[this->head].next[this->keysHead] != -1)
        this->keysHead = this->map.elems[this->head].next[this->keysHead];
    else {
        this->head = this->map.next[this->head];
        if (this->head != -1) {
            this->keysHead = this->map.elems[this->head].head;
            this->current++;
        }
    }
}

void MultiMapIterator::first() {
    this->head = this->map.head;
    current = 0;
    if (this->head != -1)
        this->keysHead = this->map.elems[this->head].head;

}