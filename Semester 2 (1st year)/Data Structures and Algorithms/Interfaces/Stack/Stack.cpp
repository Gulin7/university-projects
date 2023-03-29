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
	if (e == NULL)
		return;
	if (this->size == this->capacity)
		this->resize(this->capacity * 2);

	this->stack[this->size++] = e;
}

TElem Stack::top() const {
	//TODO - Implementation
	if (this->size != 0)
		return this->stack[this->size - 1];
	return NULL_TELEM;
}

TElem Stack::pop() {
	//TODO - Implementation
	if (this->size != 0)
		return this->stack[--this->size];
	return NULL_TELEM;
}


bool Stack::isEmpty() const {
	//TODO - Implementation
	if (this->size == 0)
		return true;
	return false;
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

}
