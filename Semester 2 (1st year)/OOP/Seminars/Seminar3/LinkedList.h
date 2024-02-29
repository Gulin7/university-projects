#pragma once

template <typename T>
class Node
{
	// TODO
};

template <typename T>
class LinkedList
{
private:
	// TODO

public:
	LinkedList(Node<T>* f = nullptr);
	LinkedList(const LinkedList& l);
	~LinkedList();

	// assignment operator for a LinkedList
	LinkedList& operator=(const LinkedList& l);

	T& operator[](int pos);

	// Adds an element to the current LinkedList.
	void add(const T& e);

	int getSize() const;
};
