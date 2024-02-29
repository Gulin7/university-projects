package item;

public class Cube implements Item{

    float volume;
    String type;

    public Cube(){}

    public Cube(float volume, String type){ this.volume = volume; this.type = type;}
    @Override
    public float getVolume() {
        return volume;
    }

    @Override
    public String getType() {
        return type;
    }

    @Override
    public boolean equals(Object obj) {
        if(!(obj instanceof Cube))
            return false;
        Cube cube = (Cube) obj;
        return cube.getVolume() == this.volume && cube.getType().equals(this.type);
    }
}
