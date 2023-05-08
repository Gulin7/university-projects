#include "MultiMap.h"
#include "MultiMapIterator.h"
#include <exception>
#include <iostream>

using namespace std;


MultiMap::MultiMap() {
	//TODO - Implementation
	this->capacity = 10000;
	this->nodes = new TElem[capacity];
	this->next = new int[capacity];
	this->sizeArray = 0;
	this->firstEmpty = 0;
	this->head = -1;
	this->tail = -1;
	for (int index = 0; index < capacity - 1; index++) {
		this->next[index] = index + 1;
	}
	this->next[capacity - 1] = -1;
}


void MultiMap::add(TKey c, TValue v) {
	//TODO - Implementation
	//resize
	if (this->sizeArray == this->capacity) {
		this->capacity *= 2;
		TElem* newNodes = new TElem[this->capacity];
		int* newNext = new int[this->capacity];
		for (int index = 0; index < capacity / 2; index++) {
			newNodes[index] = this->nodes[index];
			newNext[index] = this->next[index];
		}
		delete[] this->next;
		delete[] this->nodes;
		this->next = new int[capacity];
		this->nodes = new TElem[capacity];
		this->nodes = newNodes;
		this->next = newNext;
	}
	int prev = -1;
	int current = this->head;
	TElem elem = make_pair(c, v);
	while (current != -1 && this->nodes[current].first != c && this->nodes[current].second != v)
	{
		prev = current;
		current = this->next[current];
	}
	if (current != -1) {
		//
	}
	else {//not found
		if (this->firstEmpty == -1) {

		}
	}
}


bool MultiMap::remove(TKey c, TValue v) {
	//TODO - Implementation
	return  false;
}


vector<TValue> MultiMap::search(TKey c) const {
	//TODO - Implementation
	return vector<TValue>();
}


int MultiMap::size() const {
	//TODO - Implementation
	return this->sizeArray;
}


bool MultiMap::isEmpty() const {
	//TODO - Implementation
	if(this->sizeArray==0)
		return true;
	return false;
}

MultiMapIterator MultiMap::iterator() const {
	return MultiMapIterator(*this);
}


MultiMap::~MultiMap() {
	//TODO - Implementation
}

