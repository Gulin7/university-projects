package Controller;

import Repository.IRepository;
import Item.Item;
import RepoException.RepoException;

import java.util.ArrayList;
import java.util.List;

public class Controller {
    IRepository repo;

    public Controller(IRepository repo){
        this.repo = repo;
    }

    public void addItem(Item newItem){
        repo.addItem(newItem);
    }

    public List<Item> filter(float weight){
        List<Item> filteredItems = new ArrayList<>();
        /*for(int i=0; i<this.repo.getSize();i++){
            if(this.repo.getAll()[i].getWeight() > weight)
                filteredItems.add(this.repo.getAll()[i]);
        }*/
        for(Item it : repo.getAll()){
            if(it.getWeight()>weight)
                filteredItems.add(it);
        }
        return filteredItems;
    }

    public List<Item> getAll(){
        //return Arrays.asList(this.repo.getAll());
        //return List.of(this.repo.getAll());
        List<Item> items = new ArrayList<>();
        for(int i=0;i<this.repo.getSize();i++){
            items.add(this.repo.getAll()[i]);
        }
        return items;
    }

}
