#include "Queue.h"
#include <exception>
#include <iostream>

using namespace std;


Queue::Queue() {
	//TODO - Implementation
	this->size = 0;
	this->capacity = 1024;
	this->front = 0;
	this->rear = 0;
	this->queue =(TElem*) malloc(sizeof(TElem) * this->capacity);
}


void Queue::push(TElem elem) {
	//TODO - Implementation
	if (elem == NULL)
		return;
	if (this->size == this->capacity){
		this->capacity *= 2;
		this->queue = (TElem*) realloc(this->queue, sizeof(TElem) * this->capacity);
	}
	this->queue[this->size] = elem;
	this->size += 1;
}


TElem Queue::top() const {
	//TODO - Implementation
	if (this->size == 0)
		throw exception("Queue is empty!");
	if (this->size != 0)
		return this->queue[0];

	return NULL_TELEM;
}

TElem Queue::pop() {
	//TODO - Implementation
	if (this->size == 0)
		throw exception("Queue is empty!");

	if (this->size != 0) {
		this->size--;
		TElem toReturn = this->queue[0];
		for (int index = 0; index < size; index++)
			this->queue[index] = this->queue[index + 1];
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
	free(this->queue);
}

