package Repository;

import Item.Item;

public interface IRepository {
    void addItem(Item newItem);
    void removeItem(Item itemToRemove);
    public Item[] getAll();
    public int getSize();
}
