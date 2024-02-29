package item;

public class Sphere implements Item {

    float volume;
    String type;

    public Sphere() {
    }

    public Sphere(float volume, String type) {
        this.type = type;
        this.volume = volume;
    }

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
        if(!(obj instanceof Sphere))
            return false;
        Sphere sph = (Sphere) obj;
        return sph.getVolume() == this.volume && sph.getType().equals(this.type);
    }
}
