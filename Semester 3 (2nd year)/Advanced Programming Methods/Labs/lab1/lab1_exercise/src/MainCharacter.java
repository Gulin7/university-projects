import javax.management.RuntimeErrorException;

public class MainCharacter extends Character{
    String plotArmor;
    public MainCharacter(String name, String technique,int age, String plotArmor){
        this.name = name;
        this.technique = technique;
        this.age = age;
        this.aura = aura;
        try{
            if (plotArmor == "None"){
                throw new RuntimeException("Not a true main character.");
            }
        }
        catch(Error e){
            System.out.printf(e.getMessage());
        }
        this.plotArmor = plotArmor;
    }

    public void UseTechnique(){
        System.out.printf(this.name + " used the super " + this.technique+"!");
    }
}
