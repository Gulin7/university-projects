#pragma once
//DO NOT CHANGE THIS PART
typedef int TElem;
#define NULL_TELEM -111111

class Stack
{
private:

	//TODO - Representation
	TElem* stack;
	int capacity, size;
	
public:

	//constructor
	Stack();
	
	//pushes an element to the top of the Stack
	void push(TElem e);
	
	//returns the element from the top of the Stack
	//throws exception if the stack is empty
	TElem top() const;
	   
	//removes and returns the element from the top of the Stack
	//throws exception if the stack is empty
	TElem pop();

	// pops one occurance of the minimum element from the stack
	// all are integers;
	TElem popMinium();
	   
	//checks if the stack is empty
	bool isEmpty() const;
	
	//destructor
	~Stack();

	

private:
	void resize(int newCapacity);
};

