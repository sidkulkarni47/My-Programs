/*conditional statements*/


public class IfelseSwitch {
    public static void main(String[] args) {
        int x = 20;

        if (x < 10) {
            System.out.println("x is less than 10");
        } else if (x == 20) {
            System.out.println("x is 20");
        } else {
            System.out.println("x is greater than 10");
        }

        switch (x) {
            case 10:
                System.out.println("x is 10");
                break;
            case 20:
                System.out.println("x is 20");
                break;
            default:
                System.out.println("x is neither 10 nor 20");
                break;
        }
    }
}

