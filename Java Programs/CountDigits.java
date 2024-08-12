/*
Problem Statement - I am given a number I need to count the number of digit  
eg - 4237881
How would I count the number of digit ?
I will write a number on a paper(input is taken by the paper, paper is a variable)
I have a digital counter in my hand(a variable to store the indexs starting from 0)
Starting running throught the number thant is given to me and record the index as I pass through each number
I get 7 as the reading on the digital recorder, lets consider it as n = 7
as my recorder starts from 0 I will add a number to the reading from the recorder and that is my final result
 */



 import java.util.Scanner;

 public class CountDigits {
     public static void main(String[] args) {
 
         Scanner scanner = new Scanner(System.in);
         
         System.out.print("Enter a number: ");
         long number = scanner.nextLong();  
         int count = 0; 
 
         
         while (number > 0) {
             number /= 10; 
             count++; 
         }
 
         System.out.println("The number of digits is: " + count);
         
         scanner.close();
     }
 }
