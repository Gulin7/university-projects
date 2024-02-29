public class Character {
    String name, technique;
    int age;
    static String aura;

    public Character() {
        this.name = "";
        this.technique = "";
        this.age = 1;
    }

    public Character(String name, String technique, int age, String aura) {
        this.name = name;
        this.technique = technique;
        this.age = age;
        this.aura = aura;
    }

    public void UseTechnique() {
        System.out.printf(this.name + " used " + this.technique + "!");
    }
}
