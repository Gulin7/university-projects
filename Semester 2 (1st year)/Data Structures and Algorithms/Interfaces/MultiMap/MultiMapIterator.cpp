#include "MultiMapIterator.h"
#include "MultiMap.h"


MultiMapIterator::MultiMapIterator(const MultiMap& c): col(c) {
	//TODO - Implementation
}

TElem MultiMapIterator::getCurrent() const{
	//TODO - Implementation
	if (!this->valid())
		throw exception();
}

bool MultiMapIterator::valid() const {
	//TODO - Implementation
	if (this->keyIndex == -1) 
		return false;
	if (this->valueIndex == -1) 
		return false;
	return true;
}

void MultiMapIterator::next() {
	//TODO - Implementation
	if (!this->valid())
		throw exception();
}

void MultiMapIterator::first() {
	//TODO - Implementation

}