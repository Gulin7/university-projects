#pragma once

template <typename T>
class DynamicVector {
private:
	int capacity, size;
	T* elements;
	void resize();

public:
	//CONSTRUCTOR
	DynamicVector(int capacity = 10);

	//DESTRUCTOR
	~DynamicVector();

	//COPY CONSTRUCTOR
	DynamicVector(const DynamicVector& dynamicVectorToCopy);

	//ASSIGNMENT OPERATOR
	DynamicVector& operator=(const DynamicVector& dynamicVector);

	//METHODS
	void addElement(const T& elementToAdd);
	void removeElement(int positionToRemove);
	void updateElement(int positionToUpdate, T updatedElement);
	int getSize();
	T getElement(int positionToGet);
	int findPosition(T elementSearched);

};

template<typename T>
inline void DynamicVector<T>::resize()
{
	int newCapacity = this->capacity * 2;
	T* newElements = new T[newCapacity];
	if (newElements == nullptr)
		return;
	this->capacity = newCapacity;
	for (int index = 0; index < this->size; index++)
		newElements[index] = this->elements[index];
	delete[]this->elements;
	this->elements = newElements;
}

template<typename T>
inline DynamicVector<T>::DynamicVector(int capacity):
	capacity{capacity}, size{0}
{
	this->elements = new T[this->capacity];
}

template<typename T>
inline DynamicVector<T>::~DynamicVector()
{
	delete[] this->elements;
}

template<typename T>
inline DynamicVector<T>::DynamicVector(const DynamicVector& dynamicVectorToCopy)
{
	this->capacity = dynamicVectorToCopy.capacity;
	this->size = dynamicVectorToCopy.size;
	this->elements = new T[this->capacity];
	for (int index = 0; index < this->size; index++)
		this->elements[index] = dynamicVectorToCopy.elements[index];
}

template<typename T>
inline DynamicVector<T>& DynamicVector<T>::operator=(const DynamicVector& dynamicVector)
{
	this->capacity = dynamicVector.capacity;
	this->size = dynamicVector.size;

	delete[] this->elements;
	this->elements = new T[this->capacity];
	for (int index = 0; index < this->size; index++)
		this->elements[index] = dynamicVector.elements[index];
	return *this;
}

template<typename T>
inline void DynamicVector<T>::addElement(const T& elementToAdd)
{
	if (this->size == this->capacity)
		this->resize();
	this->elements[this->size++] = elementToAdd;
}

template<typename T>
inline void DynamicVector<T>::removeElement(int positionToRemove)
{
	if (positionToRemove < 0 || positionToRemove >= this->size)
		return;
	T* newElements = new T[this->capacity];
	for (int index = 0; index < positionToRemove; index++)
		newElements[index] = this->elements[index];

	for (int index = positionToRemove + 1; index < this->size; index++)
		newElements[index] = this->elements[index];
	delete[] this->elements;
	this->elements = newElements;
	this->size--;
}

template<typename T>
inline void DynamicVector<T>::updateElement(int positionToUpdate, T updatedElement)
{
	this->elements[positionToUpdate] = updatedElement;
}

template<typename T>
inline int DynamicVector<T>::getSize()
{
	return this->size;
}

template<typename T>
inline T DynamicVector<T>::getElement(int positionToGet)
{
	return this->elements[positionToGet];
}

template<typename T>
inline int DynamicVector<T>::findPosition(T elementSearched)
{
	for (int index = 0; index < this->size; index++)
		if (elementSearched == this->elements[index])
			return index;
	return -1;
}
