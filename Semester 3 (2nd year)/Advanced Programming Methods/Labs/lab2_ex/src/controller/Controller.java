package controller;

import item.Item;
import repoException.RepoException;
import repository.IRepository;

import java.util.ArrayList;
import java.util.List;

public class Controller {
    IRepository repo;

    public Controller(IRepository repo) {
        this.repo = repo;
    }

    public int getSize() {
        return this.repo.getSize();
    }

    public void addItem(Item newItem) throws RepoException{

        this.repo.addItem(newItem);
    }

    public Item[] filterByVolume(float volume) {
        Item[] filteredItems = new Item[100];
        int currentSize = 0;
        for (int index=0; index<this.getSize();index++) {
            if (this.getAll()[index].getVolume() > volume) {
                filteredItems[currentSize++] = this.getAll()[index];
            }
        }
        return filteredItems;
    }

    public Item[] getAll() {
        return repo.getAll();
    }

    public void removeItem(Item itemToRemove) {
        this.repo.removeItem(itemToRemove);
    }
    public boolean find(Item item){
        return this.repo.find(item);
    }
}
