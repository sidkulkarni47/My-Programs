//Problem statement - I am given a sentence of few words and asked to give the output in reverse form
//How to reverse a sentence?
// Suppose my name 'Siddhant' is written on a paper and asked to reverse it
// I will look throught spelling of the entire name(lenght) and spot the last letter, second last, third last and so on(n-1)
// I will write those letter, in technical terms I will store it on paper by writing it down(stored it in reversed sentence)
//once I am done with the entire letters in the word I get a reverse of the sentence 





public class ReverseString {
    public static void main(String[] args) {
        String sentence = "My name is Siddhant";
        String reversedSentence = "";

        // Reverse the sentence by reversing each word
        for (int i = sentence.length() - 1; i >= 0; i--) {
            reversedSentence += sentence.charAt(i);
        }

        System.out.println("Original Sentence: " + sentence);
        System.out.println("Reversed Sentence: " + reversedSentence);
    }
}

