//Hackerrank_Strings.java

// // This exercise is to test your understanding of Java Strings. A sample String declaration:

// // String myString = "Hello World!"
// // The elements of a String are called characters. The number of characters in a String is called the length, and it can be retrieved with the String.length() method.

// // Given two strings of lowercase English letters,  A and B, perform the following operations:

// // Sum the lengths of A and B.
// // Determine if A is lexicographically larger than B (i.e.: does B  come before A in the dictionary?).
// // Capitalize the first letter in A and B and print them on a single line, separated by a space.


// import java.util.*;

// public class Solution {

//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         String A = sc.next();
//         String B = sc.next();
//         sc.close();
        
//         // Calculate sum of lengths
//         int sumLengths = A.length() + B.length();
        
//         // Compare lexicographical order
//         String lexComparison = (A.compareTo(B) > 0) ? "Yes" : "No";
        
//         // Capitalize first letter of A and B
//         String capitalizedA = A.substring(0, 1).toUpperCase() + A.substring(1);
//         String capitalizedB = B.substring(0, 1).toUpperCase() + B.substring(1);
        
//         // Print results
//         System.out.println(sumLengths);
//         System.out.println(lexComparison);
//         System.out.println(capitalizedA + " " + capitalizedB);
//     }
// }




// // Given a string,s , and two indices, start and end, print a substring consisting of all characters in the inclusive range from  start to end-1. You'll find the String class' substring method helpful in completing this challenge.

// // Input Format

// // The first line contains a single string denoting s.
// // The second line contains two space-separated integers denoting the respective values of start and end.

// // Constraints
// // 1<=|s|<=100
// // 0<=start<end<=n

// // String s consists of English alphabetic letters (i.e.,[a-zA-Z] ) only.

// import java.util.*;

// public class Solution {

//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);
        
//         // Read input string
//         String s = scanner.next();
        
//         // Read start and end indices
//         int start = scanner.nextInt();
//         int end = scanner.nextInt();
        
//         scanner.close();
        
//         // Extract substring from s
//         String substring = s.substring(start, end);
        
//         // Print the substring
//         System.out.println(substring);
//     }
// }




// // A substring of a string is a contiguous block of characters in the string. For example, the substrings of abc are a, b, c, ab, bc, and abc.
// // Given a string,s , and an integer, k, complete the function so that it finds the lexicographically smallest and largest substrings of length k.

// // Function Description

// // Complete the getSmallestAndLargest function in the editor below.

// // getSmallestAndLargest has the following parameters:

// // string s: a string
// // int k: the length of the substrings to find

// // Returns
// // string: the string ' + "\n" + ' where and are the two substrings

// // Input Format
// // The first line contains a string denoting s.
// // The second line contains an integer denoting k.


// import java.util.Scanner;

// public class Solution {

//     public static String getSmallestAndLargest(String s, int k) {
//         String smallest = s.substring(0, k);
//         String largest = s.substring(0, k);
        
//         for (int i = 1; i <= s.length() - k; i++) {
//             String currentSubstring = s.substring(i, i + k);
//             if (currentSubstring.compareTo(smallest) < 0) {
//                 smallest = currentSubstring;
//             }
//             if (currentSubstring.compareTo(largest) > 0) {
//                 largest = currentSubstring;
//             }
//         }
        
//         return smallest + "\n" + largest;
//     }


//     public static void main(String[] args) {
//         Scanner scan = new Scanner(System.in);
//         String s = scan.next();
//         int k = scan.nextInt();
//         scan.close();
      
//         System.out.println(getSmallestAndLargest(s, k));
//     }
// }






// // Using Regex, we can easily match or search for patterns in a text. Before searching for a pattern, we have to specify one using some well-defined syntax.
// // In this problem, you are given a pattern. You have to check whether the syntax of the given pattern is valid.
// // Note: In this problem, a regex is only valid if you can compile it using the Pattern.compile method.

// // Input Format
// // The first line of input contains an integer N, denoting the number of test cases. The next N lines contain a string of any printable characters representing the pattern of a regex.

// // Output Format
// // For each test case, print Valid if the syntax of the given pattern is correct. Otherwise, print Invalid. Do not print the quotes.

// // Sample Input
// // 3
// // ([A-Z])(.+)
// // [AZ[a-z](a-z)
// // batcatpat(nat

// // Sample Output
// // Valid
// // Invalid
// // Invalid




// import java.util.Scanner;
// import java.util.regex.*;

// public class Solution {
//     public static void main(String[] args) {
//         Scanner in = new Scanner(System.in);
//         int testCases = Integer.parseInt(in.nextLine());
//         while (testCases > 0) {
//             String pattern = in.nextLine();
//             try {
//                 Pattern.compile(pattern);
//                 System.out.println("Valid");
//             } catch (PatternSyntaxException e) {
//                 System.out.println("Invalid");
//             }
//             testCases--;
//         }
//         in.close();
//     }
// }
