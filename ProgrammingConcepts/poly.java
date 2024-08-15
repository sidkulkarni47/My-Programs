class Animal {
    void sound() {
        System.out.println("Animal makes a sound.");
    }
}

class Cat extends Animal {
    void sound() {
        System.out.println("Cat meows.");
    }
}

public class poly {
    public static void main(String[] args) {
        Animal myAnimal = new Cat();
        myAnimal.sound();
    }
}

