#include "SortedSet.h"
#include "SortedSetIterator.h"
#include <cstdlib>

SortedSet::SortedSet(Relation r) {
	//TODO - Implementation
	this->relation = r;
	this->head = nullptr;
	this->tail = nullptr;
	this->length = 0;
}


bool SortedSet::add(TComp elem) {
	//TODO - Implementation
	// IF THE ELEMENT EXISTS WE DO NOT ADD IT
	if (this->search(elem)) {
		return false;
	}
	// WE ADD THE ELEMENT:
	// WE INCREASE THE LENGTH
	this->length++;
	// CREATE THE NODE THAT WE WANT TO ADD
	Node* newNode = new Node{ elem, nullptr, nullptr };
	// if it is the first element added in the SortedSet:
	if (this->head == nullptr) {
		this->head = newNode;
		this->tail = newNode;
		return true;
	}
	Node* currentNode = this->head;
	Node* previousNode = nullptr;
	while (currentNode != nullptr && this->relation(currentNode->data, elem)) {
		previousNode = currentNode;
		currentNode = currentNode->next;
	}
	// we will need to add on the current node:
	// IF WE ADD ON THE LAST POSITION
	if (currentNode == nullptr) {
		this->tail = newNode; // we make the tail the newNode
		currentNode = newNode; 
		newNode->prev = previousNode; // we make the newNode previous = previousNode
		previousNode->next = newNode; // we put newNode as the next for the previousNode 
		return true; // return true
	}
	// IF WE ADD ON THE FIRST POSITION
	if (previousNode == nullptr) {
		currentNode->prev = newNode;
		newNode->next = currentNode;
		this->head = newNode;
		return true;
	}
	// IF WE ADD SOMEWHERE IN THE MIDDLE
	previousNode->next = newNode;
	newNode->prev = previousNode;
	newNode->next = currentNode;
	currentNode->prev = newNode;
	return true;
	//complexity O(n) cause it iterates until it finds the place in the Set where it needs to be added
}


bool SortedSet::remove(TComp elem) {
	//TODO - Implementation
	// IF WE DO NOT FIND THE ELEMENT, WE RETURN FALSE
	if (!this->search(elem))
		return false;
	// then we search for the node
	this->length--;
	Node* currentNode = this->head;
	while (currentNode->data != elem && currentNode!=nullptr)
		currentNode = currentNode->next;
	//then we remove the current node: 
	Node* nextNode = currentNode->next;
	Node* prevNode = currentNode->prev;

	if (nextNode == nullptr && prevNode == nullptr)
	{
		this->head = nullptr;
		this->tail = nullptr;
		delete currentNode;
		return true;
	}
	if (nextNode == nullptr) {
		// in case this is the last element:
		this->tail = prevNode;
		prevNode->next = nextNode;
		delete currentNode;
		return true;
	}
	if (prevNode == nullptr) {
		this->head = nextNode; // in case this is the first element
		nextNode->prev = prevNode;
		delete currentNode;
		return true;
	}
	// if this is somewhere in the middle
	prevNode->next = nextNode;
	nextNode->prev = prevNode;
	delete currentNode;
	return true;

	// this iterates through all the nodes until it finds the one that needs to be removed => 
	// complexity O(n)
}


bool SortedSet::search(TComp elem) const {
	//TODO - Implementation
	Node* currentNode = this->head;
	while (currentNode != nullptr && currentNode->data != elem)
		currentNode = currentNode->next;
	if (currentNode == nullptr)
		return false;
	return true;
	
	// complexity O(n) , n=this->lenngth
}


int SortedSet::size() const {
	//TODO - Implementation
	return this->length;
}



bool SortedSet::isEmpty() const {
	//TODO - Implementation
	if (this->head == nullptr)
		return true;
	return false;
}

SortedSetIterator SortedSet::iterator() const {
	return SortedSetIterator(*this);
}

SortedSet::~SortedSet() {
	//TODO - Implementation
	Node* current = this->head;
	while (current != nullptr) {
		Node* next = current->next;
		delete current;
		current = next;
	}
}

int SortedSet::getRange()
{
	if (this->length == 0)
		return -1;
	return abs(this->head->data - this->tail->data);
}
