abstract class Animal {
    abstract void sound();
}

class Dog extends Animal {
    void sound() {
        System.out.println("Dog barks.");
    }
}

public class abstraction {
    public static void main(String[] args) {
        Animal myDog = new Dog();
        myDog.sound();
    }
}

