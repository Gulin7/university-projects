package repository;

import item.Item;

public interface IRepository {
    void addItem(Item newItem);

    void removeItem(Item itemToRemove);

    public Item[] getAll();

    public int getSize();

    public boolean find(Item item);
}
