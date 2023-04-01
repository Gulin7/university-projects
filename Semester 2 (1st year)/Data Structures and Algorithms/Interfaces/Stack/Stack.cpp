#include "Stack.h"
#include <exception>


using namespace std;


Stack::Stack() {
	//TODO - Implementation
	this->stack = new TElem[10];
	this->capacity = 10;
	this->size = 0;
}


void Stack::push(TElem e) {
	//TODO - Implementation
	if (e == NULL_TELEM)
		return;
	if (this->size == this->capacity)
		this->resize(this->capacity * 2);

	this->stack[this->size++] = e;
	// teta 1 best case
	// worst case it has to do a resize so n

}

TElem Stack::top() const {
	//TODO - Implementation
	if (this->size == 0)
		throw exception("Bad!");
	return this->stack[this->size - 1];
	// teta 1 every case

	
}

TElem Stack::pop() {
	//TODO - Implementation
	if (this->size == 0)
		throw exception("Bad!");
	return this->stack[--this->size];
	// teta 1 every case

}


TElem Stack::popMinium()
{
	if (this->size == 0)
		throw exception("Bad!");
	// we find the position we need to remove
	int minimum = 99999999, last_pos=0;
	for(int index=this->size-1;index>=0;index--)
		if (this->stack[index] < minimum)
		{
			minimum = this->stack[index];
			last_pos = index;
		}
	this->size--;
	for (int index = last_pos; index < this->size; index++)
		this->stack[index] = this->stack[index + 1];
	return minimum;
	// complexity is teta(n) ( at most 2*n iterations)
}

bool Stack::isEmpty() const {
	//TODO - Implementation
	if (this->size == 0)
		return true;
	return false;
	// teta 1 every case

}

Stack::~Stack() {
	//TODO - Implementation
	delete[] this->stack;
}

void Stack::resize(int newCapacity)
{
	TElem* newArray = new TElem[newCapacity];
	for (int index = 0; index < newCapacity && index < this->size; index++)
		newArray[index] = this->stack[index];

	this->capacity = newCapacity;

	delete[] this->stack;

	this->stack = newArray;
	// O(n) because it parses the whole stack once
}
