import copy

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self):
        self.size = 10
        self.count = 0
        self.list = [None] * 10

    def hash(self, value):
        if isinstance(value, int):
            return value % self.size
        hash_value = 5381
        for char in str(value):
            hash_value = ((hash_value << 5) + hash_value) + ord(char)  # hash_value * 33 + char
        return hash_value % self.size

    def insert(self, key, value):
        if self.count and (self.size // self.count < 2):
            self.resizeAndRehash()
        elem = self.list[self.hash(key)]
        if elem is None:
            self.list[self.hash(key)] = Node(key, value)
            self.count += 1
            return

        while elem.next is not None:
            elem = elem.next
        elem.next = Node(key, value)
        self.count += 1

    def get(self, key):
        elem = self.list[self.hash(key)]
        while elem is not None:
            if elem.key == key:
                return elem.value
            elem = elem.next
        return None

    def resizeAndRehash(self):
        self.size *= 2
        copyList = copy.deepcopy(self.list)
        self.list = [None] * self.size
        self.count = 0
        for elem in copyList:
            copyElem = copy.deepcopy(elem)
            while copyElem is not None:
                self.insert(copyElem.key, copyElem.value)
                copyElem = copyElem.next