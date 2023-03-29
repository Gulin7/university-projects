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
	if (elem == NULL)
		return;
	if (this->size == this->capacity){
		// we need to reallocate the memory
		this->resize(this->capacity * 2);
		this->front = 0;
		this->rear = this->size;
	}
	this->queue[this->rear] = elem;
	this->rear += 1;
	this->size += 1;
	if (this->rear > this->size)
		this->rear = 0;
}


TElem Queue::top() const {
	//TODO - Implementation
	if (this->size == 0)
		throw exception("Queue is empty!");
	if (this->size != 0)
		return this->queue[front];

	return NULL_TELEM;
}

TElem Queue::pop() {
	//TODO - Implementation
	if (this->size == 0)
		throw exception("Queue is empty!");
	if (this->size != 0) {
		this->size--;
		TElem toReturn = this->queue[front];
		this->front++;
		return toReturn;
	}
	return NULL_TELEM;
}

bool Queue::isEmpty() const {
	//TODO - Implementation
	if (this->size == 0)
		return true;
	return false;
}


Queue::~Queue() {
	//TODO - Implementation
	delete[] this->queue;
}

void Queue::resize(int newCapacity)
{
	TElem* newArray = new TElem[newCapacity];
	
	if (this->front <= this->rear)
	{
		int k = 0;
		for (int index = this->front; index < this->rear; index++)
			newArray[k++] = this->queue[index];
	}
	else {
		int k = 0;
		for (int index = this->front; index < this->capacity; index++)
			newArray[k++] = this->queue[index];
		for (int index = 0; index < this->rear; index++) {
			newArray[k++] = this->queue[index];
		}
	}
	this->capacity = newCapacity;
	
	delete[] this->queue;

	this->queue = newArray;

}


