public class SecondaryCharacter extends Character{
    //String plotArmor;
    public SecondaryCharacter(String name, String technique,int age){
        this.name = name;
        this.technique = technique;
        this.age = age;
        this.aura = aura;
        //this.plotArmor = plotArmor;
    }

    public void UseTechnique(){
        System.out.printf(this.name + " used the great " + this.technique+"!");
    }
}
