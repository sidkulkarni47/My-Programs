/*Problem statement - I am given a word which I need to check is a palindrome or not
what is palindrome - a word/sentence/number/shapes etc when reversed looks same (eg - madam)
I am given a 5 shapes(for kids) 2 stars 2 circle and 1 triangle (input)
I placed it randomly in a line and take a picture of it for my reference( storing the original input)
I am asked to check whether the sequence of shape that I placed is a palindrome or not 
I start creating a new sequence by taking out the last shape, second last shape and so one from 1 st sequence(reversing the input)
once I place all the shapes one by one I refer it to the picture that I have taken(compare it original input)
If the sequence in the picture matches the sequence created newly then it is a palindrome (using a if else statement printing out the result)
 */





public class palindrome {
    public static void main(String[] args) {
        String original = "madam";
        String reversed = "";

        // Reverse the string
        for (int i = original.length() - 1; i >= 0; i--) {
            reversed += original.charAt(i);
        }

        // Check if the original string is equal to the reversed string
        if (original.equals(reversed)) {
            System.out.println(original + " is a palindrome.");
        } else {
            System.out.println(original + " is not a palindrome.");
        }
    }
}