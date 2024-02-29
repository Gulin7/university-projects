package View;

import Controller.Controller;
import Item.Apple;
import RepoException.RepoException;
import Item.Item;

import javax.naming.ldap.Control;
    import java.util.Scanner;

    public class View {
        Controller controller;

        public View(Controller controller) {
            this.controller = controller;
        }

        public void printMenu() {
            System.out.println("0.Exit");
            System.out.println("1. Add item");
            System.out.println("2. Remove item");
            System.out.println("3. Filter items");
            System.out.println("4. Show items");
        }

        public void run() {
            do {
                printMenu();
                Scanner scanner = new Scanner(System.in);
                System.out.println("Option: ");
                String option = scanner.nextLine();

                switch (option) {
                    case "0":
                        break;
                    case "1":
                        controller.addItem(new Apple(200));
                        controller.addItem(new Apple(270));
                        controller.addItem(new Apple(250));
                        controller.addItem(new Apple(100));
                    case "2":
                        break;
                    case "3":
                        break;
                    case "4":
                        System.out.println("The items are: ");
                        for(Item it : this.controller.getAll()){
                            System.out.println("Weight: " + it.getWeight());
                        }
                }
            } while(true);
        }
    }
