package Repository;

import Item.Item;

public class MemoryIRepository implements IRepository {

    Item[] items;
    int size;

    public MemoryIRepository(){
        this.items = new Item[100];
        this.size = 0;
    }
    @Override
    public void addItem(Item newItem) {
        items[size++] = newItem;
    }

    @Override
    public void removeItem(Item itemToRemove) {
        size--;
    }

    @Override
    public Item[] getAll() {
        return items;
    }

    @Override
    public int getSize() {
        return this.size;
    }

}
