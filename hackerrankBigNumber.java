// public class hackerrankBigNumber {
// }


// // In this problem, you have to add and multiply huge numbers. These numbers are so big that you can't contain them in any ordinary data types like a long integer.
// // Use the power of Java's BigInteger class and solve this problem.
// // Input Format
// // There will be two lines containing two numbers, a and b.

// // Constraints
// // a and b are non-negative integers and can have maximum  200 digits.

// // Output Format
// // Output two lines. The first line should contain a+b, and the second line should contain a*b . Don't print any leading zeros.

// // Sample Input
// // 1234
// // 20

// // Sample Output
// // 1254
// // 24680

// // Explanation
// // 1234+20=1254
// // 1234*20=24680




// import java.math.BigInteger;
// import java.util.Scanner;

// public class Solution {
//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);
        
//         // Read the input numbers as strings
//         String a = scanner.nextLine();
//         String b = scanner.nextLine();
        
//         // Convert the strings to BigInteger
//         BigInteger num1 = new BigInteger(a);
//         BigInteger num2 = new BigInteger(b);
        
//         // Compute the sum and product
//         BigInteger sum = num1.add(num2);
//         BigInteger product = num1.multiply(num2);
        
//         // Print the results
//         System.out.println(sum);
//         System.out.println(product);
//     }
// }
