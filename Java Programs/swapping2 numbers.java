//Problem statement- Swap the 2 fruits placed in 2 boxes
// suppose someone gave you 2 boxes(box 1 and box 2) and 2 fruits(mango- box 1 and apple- box 2)
// how would you swap it ?
// I will take the help of one more box 3 to swap the fruits
// I will take out the mango from box 1 and plcae it in the box 3 for a while
// Meanwhile I will take out the apple from box 2 and place it in box1
// once this is done I will take out I will take out the fruit from box 3 and place it in the box 2
// We can consider boxes 1,2,3 as variable a,b,t and fruits as numbers 



public class test2 {
    public static void main(String[] args) {
        System.out.println("This is a program to swap a number");

        int t;
        
        int a = 5;
        int b = 6;

        System.out.println("a:"+ a +" and b:"+ b +" before swapping");

        t = a ;
        a= b;
        b= t;
        System.out.println("a:"+ a +" and b:"+ b +" after swapping");
    }
}