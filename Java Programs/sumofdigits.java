/*
 Problem Statement - I am asked to find out the number of the digits present in the entire number
I am given a number for example 2354
I will run through the number from first digit(i.e. 0th index) and get the separated digit from the number
I will write down a number on a paper(variable) 
then will add each separate number and write it on another paper
I get my desired result
 */


 import java.util.Scanner;

 public class sumofdigits {
     public static void main(String[] args) {
         /*
          Problem Statement - I am asked to find out the sum of the digits present in the entire number.
          Example: 2354
          I will run through the number from the first digit (0th index) and separate each digit.
          I will sum all the separate digits to get my desired result.
          */
 
         Scanner scanner = new Scanner(System.in);
         
         // Input the number
         System.out.print("Enter a number: ");
         String number = scanner.nextLine();  // Read the number as a string
 
         int sum = 0; // Variable to store the sum of the digits
 
         // Process each digit
         for (int i = 0; i < number.length(); i++) {
             char digitChar = number.charAt(i); // Get the character at index i
             int digit = Character.getNumericValue(digitChar); // Convert the character to an integer
 
             // Add the digit to the sum
             sum += digit; // Accumulate the sum of digits
         }
 
         // Output the result
         System.out.println("The sum of the digits is: " + sum);
         
         scanner.close();
     }
 }
 
