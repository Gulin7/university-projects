#include "MultiMapIterator.h"
#include "MultiMap.h"


MultiMapIterator::MultiMapIterator(const MultiMap& mm) : c{ mm } //theta(capacity)
{
    for (int i = 0; i < this->c.capacity; i++) {
        if (this->c.table[i].first != -1000000) {
            this->elements.push_back(this->c.table[i]);
        }
    }
    this->current = 0;
}

MultiMapIterator::~MultiMapIterator()  //theta(1)
{
}

void MultiMapIterator::first() //theta(1)
{
    this->current = 0;
}

void MultiMapIterator::next() //theta(1)
{
    if (this->valid()) {
        this->current += 1;
    }
    else {
        throw std::exception("Stop iteration\n");
    }
}

bool MultiMapIterator::valid() const //theta(1)
{
    if (this->current < this->elements.size()) {
        return true;
    }
    else {
        return false;
    }
}

TElem MultiMapIterator::getCurrent() const //theta(1)
{
    if (this->valid()) {
        return this->elements[this->current];
    }
    else {
        throw std::exception("invalid element\n");
    }
}