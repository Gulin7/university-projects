package Item;

import Item.Item;

public class Apple implements Item {
    float weight;

    public Apple(){};

    public Apple(float weight){
        this.weight=weight;
    }
    @Override
    public float getWeight() {
        return this.weight;
    }
}
