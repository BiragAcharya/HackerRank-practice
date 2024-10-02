//Hackerrank_Introduction.java



// // Welcome to the world of Java! In this challenge, we practice printing to stdout.
// // The code stubs in your editor declare a Solution class and a main method. 
// // Complete the main method by copying the two lines of code below and pasting them inside the body of your main method.

// // System.out.println("Hello, World.");
// // System.out.println("Hello, Java.");

// public class Solution {
//     public static void main(String[] args) {
//         System.out.println("Hello, World.");
//         System.out.println("Hello, Java.");
//     }
// }


// // Input Stream as System.in. For example:

// // Scanner scanner = new Scanner(System.in);
// // String myString = scanner.next();
// // int myInt = scanner.nextInt();
// // scanner.close();

// // System.out.println("myString is: " + myString);
// // System.out.println("myInt is: " + myInt);
// // The code above creates a Scanner object named  and uses it to read a String and an int.
// //  It then closes the Scanner object because there is no more input to read, and prints to stdout using System.out.println(String). So, if our input is:

// // Hi 5
// // Our code will print:

// // myString is: Hi
// // myInt is: 5



// // In this challenge, you must read  integers from stdin and then print them to stdout. Each integer must be printed on a new line.\
// //  To make the problem a little easier, a portion of the code is provided for you in the editor below.
// // Input Format
// // There are  lines of input, and each line contains a single integer.

// // Sample Input
// // 42
// // 100
// // 125



// import java.util.Scanner;

// public class Solution {
//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);

//         // Assuming we need to read exactly 3 integers as per the sample input
//         // If the number of lines is dynamic, read it first
//         int n = 3;

//         for (int i = 0; i < n; i++) {
//             int num = scanner.nextInt();
//             System.out.println(num);
//         }
//         scanner.close();
//     }
// }




// // Task
// // Given an integer, , perform the following conditional actions:

// // If  is odd, print Weird
// // If  is even and in the inclusive range of  to , print Not Weird
// // If  is even and in the inclusive range of  to , print Weird
// // If  is even and greater than , print Not Weird
// // Complete the stub code provided in your editor to print whether or not  is weird.

// // Input Format
// // A single line containing a positive integer, .
// // Constraints

// // Output Format
// // Print Weird if the number is weird; otherwise, print Not Weird.




// import java.util.Scanner;

// public class Solution {
//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);
        
//         int n = scanner.nextInt();
//         scanner.close();
        
//         if (n % 2 != 0) {
//             System.out.println("Weird");
//         } else {
//             if (n >= 2 && n <= 5) {
//                 System.out.println("Not Weird");
//             } else if (n >= 6 && n <= 20) {
//                 System.out.println("Weird");
//             } else if (n > 20) {
//                 System.out.println("Not Weird");
//             }
//         }
//     }
// }





// // In this challenge, you must read an integer, a double, and a String from stdin, then print the values according to the instructions
// //  in the Output Format section below. To make the problem a little easier, a portion of the code is provided for you in the editor.
// // Note: We recommend completing Java Stdin and Stdout I before attempting this challenge.

// // Input Format
// // There are three lines of input:
// // The first line contains an integer.
// // The second line contains a double.
// // The third line contains a String.

// // Output Format
// // There are three lines of output:
// // On the first line, print String: followed by the unaltered String read from stdin.
// // On the second line, print Double: followed by the unaltered double read from stdin.
// // On the third line, print Int: followed by the unaltered integer read from stdin.
// // To make the problem easier, a portion of the code is already provided in the editor.

// // Note: If you use the nextLine() method immediately following the nextInt() method, recall that nextInt() reads integer tokens;
// //  because of this, the last newline character for that line of integer input is still queued in the input buffer and the next nextLine() will be reading the remainder of the integer line (which is empty).



// import java.util.Scanner;

// public class Solution {
//     public static void main(String[] args) {
//         Scanner scan = new Scanner(System.in);
//         int i = scan.nextInt();

//         double d = scan.nextDouble();

//         scan.nextLine();

//         String s = scan.nextLine();

//         scan.close();

//         System.out.println("String: " + s);
//         System.out.println("Double: " + d);
//         System.out.println("Int: " + i);
//     }
// }





// // Java's System.out.printf function can be used to print formatted output. The purpose of this exercise is to test your understanding of formatting output using printf.
// // To get you started, a portion of the solution is provided for you in the editor; you must format and print the input to complete the solution.

// // Input Format
// // Every line of input will contain a String followed by an integer.
// // Each String will have a maximum of  alphabetic characters, and each integer will be in the inclusive range from  to .

// // Output Format
// // In each line of output there should be two columns:
// // The first column contains the String and is left justified using exactly  characters.
// // The second column contains the integer, expressed in exactly  digits; if the original input has less than three digits, you must pad your output's leading digits with zeroes.

// // Sample Input
// // java 100
// // cpp 65
// // python 50
// // Sample Output

// // ================================
// // java           100 
// // cpp            065 
// // python         050 
// // ================================
// // Explanation
// // Each String is left-justified with trailing whitespace through the first  characters. The leading digit of the integer is the  character, and each integer that was less than  digits now has leading zeroes.



// import java.util.Scanner;

// public class Solution {
//     public static void main(String[] args) {
//             Scanner sc=new Scanner(System.in);
//             System.out.println("================================");
//             for(int i=0;i<3;i++){
//                 String s1=sc.next();
//                 int x=sc.nextInt();
//                 System.out.printf("%-15s%03d%n", s1, x);
//             }
//             System.out.println("================================");

//             sc.close();
//     }
// }




// // Objective
// // In this challenge, we're going to use loops to help us do some simple math.

// // Task
// // Given an integer,N , print its first 10 multiples. Each multiple N * i (where 1<=i<=10 ) should be printed on a new line in the form: N x i = result.

// // Input Format
// // A single integer,N .

// // Constraints
// // 2<=N<=20

// // Output Format
// // Print 10 lines of output; each line  (where 1<=i<=10 ) contains the result of N * i in the form:
// // N x i = result.


// import java.util.Scanner;

// public class Solution {
//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);
        
//         // Read the integer N
//         int N = scanner.nextInt();
        
//         // Loop from 1 to 10
//         for (int i = 1; i <= 10; i++) {
//             int result = N * i;
//             System.out.printf("%d x %d = %d%n", N, i, result);
//         }
        
//         scanner.close();
//     }
// }




// // We use the integers a,b , and n to create the following series:
// // (a+2^0⋅b),(a+2^0⋅b+2^1⋅b),…,(a+2^0⋅b+2^1⋅b+…+2^n−1⋅b)

// // You are given q queries in the form of a, b, and n. For each query, print the series corresponding to the given a, b, and c values
// //  as a single line of n space-separated integers.

// // Input Format

// // The first line contains an integer, q, denoting the number of queries.
// // Each line i of the q subsequent lines contains three space-separated integers describing the respective ai, bi, and ni values for that query.

// // Constraints
// // 0<=q<=500
// // 0<=a,b<=50
// // 1<=n<=15

// // Output Format
// // For each query, print the corresponding series on a new line. Each series must be printed in order as a single line of  space-separated integers.


// import java.util.Scanner;

// public class Solution {
//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);
        
//         int q = scanner.nextInt(); // number of queries
        
//         for (int i = 0; i < q; i++) {
//             int a = scanner.nextInt();
//             int b = scanner.nextInt();
//             int n = scanner.nextInt();
            
//             // Generate the series for the current query
//             int currentSum = a;
//             for (int j = 0; j < n; j++) {
//                 currentSum += (int)Math.pow(2, j) * b;
//                 System.out.print(currentSum + " ");
//             }
//             System.out.println(); // New line after each query
//         }
        
//         scanner.close();
//     }
// }




// // Java has 8 primitive data types; char, boolean, byte, short, int, long, float, and double. For this exercise, we'll work with the primitives used to hold integer values (byte, short, int, and long):

// // A byte is an 8-bit signed integer.
// // A short is a 16-bit signed integer.
// // An int is a 32-bit signed integer.
// // A long is a 64-bit signed integer.
// // Given an input integer, you must determine which primitive data types are capable of properly storing that input.

// // To get you started, a portion of the solution is provided for you in the editor.

// // Reference: https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html

// // Input Format
// // The first line contains an integer,T , denoting the number of test cases.
// // Each test case,T , is comprised of a single line with an integer, , which can be arbitrarily large or small.

// // Output Format
// // For each input variable n and appropriate primitive dataType, you must determine if the given primitives are capable of storing it. If yes, then print:


// import java.util.*;
// import java.io.*;

// class Solution {
//     public static void main(String []argh) {
//         Scanner sc = new Scanner(System.in);
//         int t = sc.nextInt();

//         for (int i = 0; i < t; i++) {
//             try {
//                 long x = sc.nextLong();
//                 System.out.println(x + " can be fitted in:");
//                 if (x >= -128 && x <= 127) System.out.println("* byte");
//                 if (x >= -32768 && x <= 32767) System.out.println("* short");
//                 if (x >= -2147483648L && x <= 2147483647L) System.out.println("* int");
//                 if (x >= -9223372036854775808L && x <= 9223372036854775807L) System.out.println("* long");
//             } catch (Exception e) {
//                 System.out.println(sc.next() + " can't be fitted anywhere.");
//             }
//         }
//         sc.close();
//     }
// }




// // "In computing, End Of File (commonly abbreviated EOF) is a condition in a computer operating system where no more data can be read from a data source." — (Wikipedia: End-of-file)

// // The challenge here is to read  lines of input until you reach EOF, then number and print all  lines of content.
// // Hint: Java's Scanner.hasNext() method is helpful for this problem.

// // Input Format
// // Read some unknown  lines of input from stdin(System.in) until you reach EOF; each line of input contains a non-empty String.

// // Output Format
// // For each line, print the line number, followed by a single space, and then the line content received as input.


// import java.util.Scanner;

// public class ReadUntilEOF {
//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);
//         int lineNumber = 0;
        
//         while (scanner.hasNext()) {
//             String line = scanner.nextLine();
//             lineNumber++;
//             System.out.println(lineNumber + " " + line);
//         }
        
//         scanner.close();
//     }
// }




// // Static initialization blocks are executed when the class is loaded, and you can initialize static variables in those blocks.
// // It's time to test your knowledge of Static initialization blocks. You can read about it here.
// // You are given a class Solution with a main method. Complete the given code so that it outputs the area of a parallelogram with breadth  and height . You should read the variables from the standard input.

// // If  or  , the output should be "java.lang.Exception: Breadth and height must be positive" without quotes.

// // Input Format
// // There are two lines of input. The first line contains : the breadth of the parallelogram. The next line contains : the height of the parallelogram.

// // Constraints

// // Output Format


// // If both values are greater than zero, then the main method must output the area of the parallelogram. Otherwise, print "java.lang.Exception: Breadth and height must be positive" without quotes.


// import java.io.*;
// import java.util.*;
// import java.text.*;
// import java.math.*;
// import java.util.regex.*;

// public class Solution {
//     static int B;
//     static int H;
//     static boolean flag = true;

//     static {
//         Scanner scanner = new Scanner(System.in);
//         B = scanner.nextInt();
//         H = scanner.nextInt();

//         if (B <= 0 || H <= 0) {
//             flag = false;
//             System.out.println("java.lang.Exception: Breadth and height must be positive");
//         }
//     }

// public static void main(String[] args){
// 		if(flag){
// 			int area=B*H;
// 			System.out.print(area);
// 		}
		
// 	}//end of main

// }//end of class





// // You are given an integer n, you have to convert it into a string.

// // Please complete the partially completed code in the editor.
// //  If your code successfully converts n into a string s the code will print "Good job". Otherwise it will print "Wrong answer".
// //  n can range between -100 to 100  inclusive.

// // Sample Input 0
// // 100
// // Sample Output 0


// import java.util.*;
// import java.security.*;
// public class Solution {
//  public static void main(String[] args) {

//   DoNotTerminate.forbidExit();

//   try {
//    Scanner in = new Scanner(System.in);
//    int n = in .nextInt();
//    in.close();
//    //String s=???; Complete this line below

//     String s = Integer.toString(n);

   
//    if (n == Integer.parseInt(s)) {
//     System.out.println("Good job");
//    } else {
//     System.out.println("Wrong answer.");
//    }
//   } catch (DoNotTerminate.ExitTrappedException e) {
//    System.out.println("Unsuccessful Termination!!");
//   }
//  }
// }






// //The following class will prevent you from terminating the code using exit(0)!
// class DoNotTerminate {

//  public static class ExitTrappedException extends SecurityException {

//   private static final long serialVersionUID = 1;
//  }

//  public static void forbidExit() {
//   final SecurityManager securityManager = new SecurityManager() {
//    @Override
//    public void checkPermission(Permission permission) {
//     if (permission.getName().contains("exitVM")) {
//      throw new ExitTrappedException();
//     }
//    }
//   };
//   System.setSecurityManager(securityManager);
//  }
// }



// or


// import java.util.Scanner;

// public class Solution {
//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);
//         int n = scanner.nextInt();
//         scanner.close();
        
//         String s = Integer.toString(n); // Convert integer to string
        
//         // Compare the result with expected output
//         if (s.equals("100")) {
//             System.out.println("Good job");
//         } else {
//             System.out.println("Wrong answer");
//         }
//     }
// }






// // The Calendar class is an abstract class that provides methods for converting between a specific instant in time and a set of calendar fields such as
// //  YEAR, MONTH, DAY_OF_MONTH, HOUR, and so on, and for manipulating the calendar fields, such as getting the date of the next week.

// // You are given a date. You just need to write the method,getDay , which returns the day on that date.
// //  To simplify your task, we have provided a portion of the code in the editor.
// // Example
// // month=8
// // day=14
// // year=2017


// // The method should return Monday as the day on that date.
// // image
// // Function Description
// // Complete the findDay function in the editor below.
// // findDay has the following parameters:

// // int: month
// // int: day
// // int: year
// // Returns

// // string: the day of the week in capital letters


// import java.io.*;
// import java.math.*;
// import java.security.*;
// import java.text.*;
// import java.util.*;
// import java.util.concurrent.*;
// import java.util.regex.*;

// class Result {

//     /*
//      * Complete the 'findDay' function below.
//      *
//      * The function is expected to return a STRING.
//      * The function accepts following parameters:
//      *  1. INTEGER month
//      *  2. INTEGER day
//      *  3. INTEGER year
//      */

//     public static String findDay(int month, int day, int year) {
//                 // Create a Calendar instance
//         Calendar calendar = Calendar.getInstance();
//         // Set the date components
//         calendar.set(year, month - 1, day); // Note: month is 0-based in Calendar
        
//         // Get the day of the week as an integer (1=Sunday, 2=Monday, ..., 7=Saturday)
//         int dayOfWeek = calendar.get(Calendar.DAY_OF_WEEK);
        
//         // Array of day names corresponding to Calendar days
//         String[] days = {"", "SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"};
        
//         // Return the day of the week
//         return days[dayOfWeek];

//     }

// }

// public class Solution {
//     public static void main(String[] args) throws IOException {
//         BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
//         BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

//         String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

//         int month = Integer.parseInt(firstMultipleInput[0]);

//         int day = Integer.parseInt(firstMultipleInput[1]);

//         int year = Integer.parseInt(firstMultipleInput[2]);

//         String res = Result.findDay(month, day, year);

//         bufferedWriter.write(res);
//         bufferedWriter.newLine();

//         bufferedReader.close();
//         bufferedWriter.close();
//     }
// }





// // Given a double-precision number, , denoting an amount of money, use the NumberFormat class' getCurrencyInstance method to convert 
// //  into the US, Indian, Chinese, and French currency formats. Then print the formatted values as follows:

// // US: formattedPayment
// // India: formattedPayment
// // China: formattedPayment
// // France: formattedPayment
// // where  is  formatted according to the appropriate Locale's currency.

// // Note: India does not have a built-in Locale, so you must construct one where the language is en (i.e., English).


// import java.util.*;
// import java.text.*;

// public class Solution {
    
//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);
//         double payment = scanner.nextDouble();
//         scanner.close();
        
//         // Formatting for US Dollar
//         NumberFormat usFormat = NumberFormat.getCurrencyInstance(Locale.US);
//         String us = usFormat.format(payment);
        
//         // Formatting for Indian Rupee
//         Locale indiaLocale = new Locale("en", "IN");
//         NumberFormat indiaFormat = NumberFormat.getCurrencyInstance(indiaLocale);
//         String india = indiaFormat.format(payment);
        
//         // Formatting for Chinese Yuan
//         NumberFormat chinaFormat = NumberFormat.getCurrencyInstance(Locale.CHINA);
//         String china = chinaFormat.format(payment);
        
//         // Formatting for Euro
//         NumberFormat franceFormat = NumberFormat.getCurrencyInstance(Locale.FRANCE);
//         String france = franceFormat.format(payment);
        
//         // Printing formatted values
//         System.out.println("US: " + us);
//         System.out.println("India: " + india);
//         System.out.println("China: " + china);
//         System.out.println("France: " + france);
//     }
// }




