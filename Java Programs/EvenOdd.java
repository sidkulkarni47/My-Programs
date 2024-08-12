/*
    Problem Statement - I am given a number I need to check how many even or odd numbers are present in the number provided
    I am given a number on a paper eq - 23456(paper is a varibale for input)
    I will run throught the number starting from first(or index 0) and separate each number.
    I will write each number that is separated on the piece of paper(variable)
    I will divide that number with 2, will check the remainder if it is equal to 0(even), if not equal to 0(odd)
    If the number is equal to zero I will write down it in a list on a paper (array named even)
    If the number not equal to zero I will write down it in different list on a paper(array named odd)
    I will take one more paper(variable), after nrunning through the list of even and odd respectively will note it down
    Hence I get my result
 */


 import java.util.Scanner;

 public class EvenOdd {
     public static void main(String[] args) {

         Scanner scanner = new Scanner(System.in);
         
         
         System.out.print("Enter a number: ");
         String number = scanner.nextLine();  
 
         int evenCount = 0; 
         int oddCount = 0;  
 
        
         for (int i = 0; i < number.length(); i++) {
             char digitChar = number.charAt(i); 
             int digit = Character.getNumericValue(digitChar); 
 
             // Check if the digit is even or odd
             if (digit % 2 == 0) {
                 evenCount++; 
             } else {
                 oddCount++;  
             }
         }
 
         
         System.out.println("Even digits count: " + evenCount);
         System.out.println("Odd digits count: " + oddCount);
         
         scanner.close();
     }
 }
 
