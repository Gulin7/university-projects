package repository;

import item.Item;
import repoException.RepoException;

import javax.lang.model.type.NullType;

public class MemoryRepository implements IRepository {
    Item[] items;
    int size;

    public MemoryRepository() {
        this.items = new Item[100];
        this.size = 0;
    }

    @Override
    public void addItem(Item newItem) throws RepoException {
        if (this.getSize() > 99)
            throw new RepoException("Too many elements!");
        this.items[size++] = newItem;
    }

    @Override
    public void removeItem(Item itemToRemove) {

        int currentSize = 0;
        for (int index = 0; index < this.getSize(); index++) {
            if (!this.items[index].equals(itemToRemove))
                this.items[currentSize++] = this.items[index];
        }
        for (int index = currentSize; index < this.size; index++)
            this.items[index] = null;
        this.size = currentSize;
    }

    @Override
    public Item[] getAll() {
        return items;
    }

    @Override
    public int getSize() {
        return this.size;
    }

    public boolean find(Item item) {
        for (int index = 0; index < this.getSize(); index++) {
            if (this.items[index].equals(item))
                return true;
        }
        return false;
    }
}
