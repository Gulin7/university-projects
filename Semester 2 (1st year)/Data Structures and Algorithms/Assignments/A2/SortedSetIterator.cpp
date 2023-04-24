#include "SortedSetIterator.h"
#include <exception>

using namespace std;

SortedSetIterator::SortedSetIterator(const SortedSet& m) : multime(m)
{
	//TODO - Implementation
	this->currentNode = this->multime.head;
}


void SortedSetIterator::first() {
	//TODO - Implementation
	this->currentNode = this->multime.head;
}


void SortedSetIterator::next() {
	//TODO - Implementation
	if (!this->valid())
		throw exception("Bad");
	this->currentNode = this->currentNode->next;
}	


TElem SortedSetIterator::getCurrent()
{
	//TODO - Implementation
	if (!(this->valid()))
		throw exception("Bad");
	return this->currentNode->data;
}

bool SortedSetIterator::valid() const {
	//TODO - Implementation
	if (this->currentNode == nullptr)
		return false;
	return true;
}

