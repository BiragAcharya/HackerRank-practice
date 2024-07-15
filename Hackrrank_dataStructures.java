// public class Hackrrank_dataStructures {
    
// }



// // To create an array of integers named  that can hold four integer values, you would write the following code:

// // int[] myArray = new int[4];
// // This sets aside a block of memory that's capable of storing  integers. Each integer storage cell is assigned a unique index ranging from  to one less than the size of the array, and each cell initially contains a . In the case of , we can store integers at indices , , , and . Let's say we wanted the last cell to store the number ; to do this, we write:

// // myArray[3] = 12;
// // Similarly, we can print the contents of the last cell with the following code:

// // System.out.println(myArray[3]);
// // The code above prints the value stored at index  of , which is  (the value we previously stored there). It's important to note that while Java initializes each cell of an array of integers with a , not all languages do this.

// // Task
// // Task

// // The code in your editor does the following:

// // Reads an integer from stdin and saves it to a variable, , denoting some number of integers.
// // Reads n integers corresponding to a0,a1,...,an-1 from stdin and saves each integer ai to a variable, val.
// // Attempts to print each element of an array of integers named .
// // Write the following code in the unlocked portion of your editor:

// // Create an array,a , capable of holding n integers.
// // Modify the code in the loop so that it saves each sequential value to its corresponding location in the array. For example, the first value must be stored in a0, the second value must be stored in a1, and so on.
// // Good luck!

// // Input Format

// // The first line contains a single integer, , denoting the size of the array.
// // Each line i of the n subsequent lines contains a single integer denoting the value of element ai.

// // Output Format

// // You are not responsible for printing any output to stdout. Locked code in the editor loops through array a and prints each sequential element on a new line.



// import java.util.*;

// public class Solution {

//     public static void main(String[] args) {
	   
//         Scanner scan = new Scanner(System.in);
//         int n = scan.nextInt();
//         int[] a = new int[n];
        
//         for (int i = 0; i < n; i++) {
//             a[i] = scan.nextInt();
//         }
        
//         scan.close();

//         // Prints each sequential element in array a
//         for (int i = 0; i < a.length; i++) {
//             System.out.println(a[i]);
//         }
//     }
// }






// // You are given a 6*6 2D array. An hourglass in an array is a portion shaped like this:

// // a b c
// //   d
// // e f g
// // For example, if we create an hourglass using the number 1 within an array full of zeros, it may look like this:

// // 1 1 1 0 0 0
// // 0 1 0 0 0 0
// // 1 1 1 0 0 0
// // 0 0 0 0 0 0
// // 0 0 0 0 0 0
// // 0 0 0 0 0 0

// // Actually, there are many hourglasses in the array above. The three leftmost hourglasses are the following:
// // 1 1 1     1 1 0     1 0 0
// //   1         0         0
// // 1 1 1     1 1 0     1 0 0
// // The sum of an hourglass is the sum of all the numbers within it. The sum for the hourglasses above are 7, 4, and 2, respectively.
// // In this problem you have to print the largest sum among all the hourglasses in the array.

// // Input Format
// // There will be exactly 6 lines, each containing 6 integers seperated by spaces. Each integer will be between -9 and 9 inclusive.

// // Output Format
// // Print the answer to this problem on a single line.

// // Sample Input
// // 1 1 1 0 0 0
// // 0 1 0 0 0 0
// // 1 1 1 0 0 0
// // 0 0 2 4 4 0
// // 0 0 0 2 0 0
// // 0 0 1 2 4 0

// // Sample Output
// // 19
// // Explanation

// // The hourglass which has the largest sum is:
// // 2 4 4
// //   2
// // 1 2 4



// import java.util.Scanner;

// public class Solution {

//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);
//         int[][] arr = new int[6][6];
        
//         // Read the 6x6 array
//         for (int i = 0; i < 6; i++) {
//             for (int j = 0; j < 6; j++) {
//                 arr[i][j] = scanner.nextInt();
//             }
//         }
        
//         scanner.close();

//         // Initialize the maximum sum to the lowest possible value
//         int maxSum = Integer.MIN_VALUE;
        
//         // Loop through all possible hourglass top-left starting points
//         for (int i = 0; i <= 3; i++) {
//             for (int j = 0; j <= 3; j++) {
//                 // Calculate the sum of the current hourglass
//                 int currentSum = arr[i][j] + arr[i][j+1] + arr[i][j+2]
//                                 + arr[i+1][j+1]
//                                 + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2];
                
//                 // Update the maximum sum if the current hourglass sum is greater
//                 if (currentSum > maxSum) {
//                     maxSum = currentSum;
//                 }
//             }
//         }
        
//         // Print the maximum hourglass sum
//         System.out.println(maxSum);
//     }
// }
