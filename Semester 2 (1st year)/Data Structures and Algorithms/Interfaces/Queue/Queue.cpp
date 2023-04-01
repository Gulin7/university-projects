#include "Queue.h"
#include <exception>
#include <iostream>

using namespace std;


Queue::Queue() {
	//TODO - Implementation
	this->size = 0;
	this->capacity = 10;
	this->front = 0;
	this->rear = 0;
	this->queue = new TElem[10];
}


void Queue::push(TElem elem) {
	//TODO - Implementation
	if (this->size == this->capacity){
		// we need to reallocate the memory
		this->resize(this->capacity * 2);
		this->front = 0;
		this->rear = this->size;
	}
	this->queue[this->rear] = elem;
	this->rear = (this->rear + 1) % this->capacity;			
	this->size += 1;
	// worst case : resize => n
	// best case: 1
}


TElem Queue::top() const {
	//TODO - Implementation
	if (this->size == 0)
		throw exception("Queue is empty!");
	if (this->size != 0)
		return this->queue[front];
	// 1 in every case
	return NULL_TELEM;
}

TElem Queue::pop() {
	//TODO - Implementation
	if (this->size == 0)
		throw exception("Queue is empty!");
	if (this->size != 0) {
		this->size--;
		TElem toReturn = this->queue[front];
		this->front = (this->front+1)%this->capacity;
		return toReturn;
	}
	// teta 1 every case
	return NULL_TELEM;
}

bool Queue::isEmpty() const {
	//TODO - Implementation
	if (this->size == 0)
		return true;
	return false;
	// teta 1 every case

}


Queue::~Queue() {
	//TODO - Implementation
	delete[] this->queue;
}

void Queue::resize(int newCapacity)
{
	TElem* newArray = new TElem[newCapacity];
	
	for (int index = 0; index < this->size; index++)
		newArray[index] = this->queue[(index + this->front) % this->capacity];

	this->capacity = newCapacity;
	
	delete[] this->queue;

	this->queue = newArray;
	// o(n) ; it parses through all the stack everytime
}


