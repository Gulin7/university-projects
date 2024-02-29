package view;

import java.util.Scanner;

import controller.Controller;
import item.Cube;
import item.Item;
import item.Sphere;
import repoException.RepoException;

public class View {
    Controller controller;

    public View(Controller controller) {
        this.controller = controller;
    }

    public void printMenu() {
        System.out.println("0.Exit");
        System.out.println("1. Add item");
        System.out.println("2. Filter items");
        System.out.println("3. Show items");
        System.out.println("4. Remove item");
    }

    public void run() {
        int running = 1;
        do {
            try {
                printMenu();
                Scanner scanner = new Scanner(System.in);
                System.out.println("Option: ");
                String option = scanner.nextLine();
                switch (option) {
                    case "0":
                        running = 0;
                        break;
                    case "1":
                        System.out.println("Enter type: ");
                        String type = scanner.nextLine();
                        System.out.println("Enter volume: ");
                        float volume = Integer.parseInt(scanner.nextLine());
                        if (type.equalsIgnoreCase("cube")) {
                            Cube cube = new Cube(volume, "cube");
                            this.controller.addItem(cube);
                        } else if (type.equalsIgnoreCase("sphere")) {
                            Sphere sphere = new Sphere(volume, "sphere");
                            this.controller.addItem(sphere);
                        } else
                            throw new RepoException("Invalid type!");
                        break;
                    case "2":
                        System.out.println("Enter volume: ");
                        float volume2 = Integer.parseInt(scanner.nextLine());
                        Item[] filteredItems = this.controller.filterByVolume(volume2);
                        for (int index = 0; index < filteredItems.length; index++) {
                            if (filteredItems[index] == null)
                                break;
                            System.out.println("Volume: " + filteredItems[index].getVolume()
                                    + " type: " + filteredItems[index].getType());
                        }
                        break;
                    case "3":
                        for (int index = 0; index < this.controller.getSize(); index++)
                            System.out.println("Volume: " + this.controller.getAll()[index].getVolume()
                                    + " type: " + this.controller.getAll()[index].getType());
                        break;
                    case "4":
                        System.out.println("Enter type: ");
                        String typeToRemove = scanner.nextLine();
                        System.out.println("Enter volume: ");
                        float volumeToRemove = Integer.parseInt(scanner.nextLine());
                        if (!typeToRemove.equals("cube") && !typeToRemove.equals("sphere"))
                            throw new RepoException("Invalid type!");
                        if (typeToRemove.equals("cube")) {
                            Cube cube = new Cube(volumeToRemove, typeToRemove);
                            //System.out.println("Got here");
                            if (!controller.find(cube))
                                throw new RepoException("Item not found!");
                            controller.removeItem(cube);
                        } else {
                            Sphere sphere = new Sphere(volumeToRemove, typeToRemove);
                            if (!controller.find(sphere))
                                throw new RepoException("Item not found!");
                            controller.removeItem(sphere);
                        }
                        break;
                }
            } catch (RepoException | NumberFormatException e ) {
                System.out.println(e.getMessage());
            }
        } while (running != 0);
    }
}