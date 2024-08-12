// how to find the median ?
// Approach is to think in a simple way first
// What is the median ? Median is the middle number in the number list
//for odd its middle, for even middle two but the higher one
//A random number list is given to me
//first I will sort it in ascending manner
// Technical thinking
//scan through the list, technically will consider the indexes of list/ array
//So index starts from 0,1,2,3,4,5 for 6 number size of n is 5 
//will divide n/2 i.e. 5/2 = 2.5 rounding up the value to higher number 3 
// index of 3 is the median for even number list
//for odd number I will suppose index 0,1,2,3,4 n = 4
// divide n by 2 i.e 2 is the median





import java.util.Arrays;

public class median {
    public static void main(String[] args) {
        int[] numbers = {12, 4, 5, 3, 8, 7};

        // Sort the array
        Arrays.sort(numbers);

        // Find the median
        double median;
        int n = numbers.length;
        if (n % 2 == 0) {
            // If the array length is even, take the average of the two middle elements
            median = ((double) numbers[n/2 - 1] + numbers[n/2]) / 2;
        } else {
            // If the array length is odd, take the middle element
            median = numbers[n/2];
        }

        System.out.println("The median is: " + median);
    }
}

