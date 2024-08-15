/* This is an example for classes and object */


class Car {
    String model;
    int year;

    void drive() {
        System.out.println("The car is driving.");
    }
}

public class ClaasesObject {
    public static void main(String[] args) {
        Car myCar = new Car();
        myCar.model = "Toyota";
        myCar.year = 2020;
        myCar.drive();
    }
}
