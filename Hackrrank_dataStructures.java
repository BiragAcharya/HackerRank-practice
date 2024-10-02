// public class Hackrrank_dataStructures {
// }

// // To create an array of integers named  that can hold four integer values,you would write the following code:

// // int[] myArray = new int[4];
// // This sets aside a block of memory that's capable of storing  integers. Each integer storage cell is assigned a unique index ranging from  to one less than the size of the array, and each cell initially contains a . In the case of , we can store integers at indices , , , and . Let's say we wanted the last cell to store the number ; to do this, we write:

// // myArray[3] = 12;
// // Similarly, we can print the contents of the last cell with the following code:

// // System.out.println(myArray[3]);
// // The code above prints the value stored at index  of , which is  (the value we previously stored there). It's important to note that while Java initializes each cell of an array of integers with a , not all languages do this.



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






// // For this problem, we have 2 types of queries you can perform on a List:

// // Insert y at index x:

// // Insert
// // x y
// // Delete the element at index x:

// // Delete
// // x
// // Given a list, L , of N integers, perform Q queries on the list. Once all queries are completed, print the modified list as a single line of space-separated integers.

// // Input Format
// // The first line contains an integer,N  (the initial number of elements in L).
// // The second line contains N space-separated integers describing L.
// // The third line contains an integer,Q  (the number of queries).
// // The 2Q subsequent lines describe the queries, and each query is described over two lines:

// // If the first line of a query contains the String Insert, then the second line contains two space separated integers x y, and the value y must be inserted into L at index x.
// // If the first line of a query contains the String Delete, then the second line contains index x, whose element must be deleted from L .
// // Constraints
// // 1<=N<=4000
// // 1<=Q<=4000

// // Each element in is a 32-bit integer.
// // Output Format
// // Print the updated list L as a single line of space-separated integers.

// // Sample Input
// // 5
// // 12 0 1 78 12
// // 2
// // Insert
// // 5 23
// // Delete
// // 0

// // Sample Output
// // 0 1 78 12 23
// // Explanation
// // L=[12,0,1,78,12]
// //  Q0 : Insert 23 at index .
// // L0=[12,0,1,78,12,23]
// //  Q1:Delete the element at index .
// // L1=[0,1,78,12,23]

// // Having performed all Q queries, we print L1 as a single line of space-separated integers.




// import java.io.*;
// import java.util.*;

// public class Solution {
//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);
        
//         // Read initial number of elements
//         int N = scanner.nextInt();
//         List<Integer> L = new ArrayList<>();
        
//         // Read the initial list of elements
//         for (int i = 0; i < N; i++) {
//             L.add(scanner.nextInt());
//         }
        
//         // Read the number of queries
//         int Q = scanner.nextInt();
        
//         // Process each query
//         for (int i = 0; i < Q; i++) {
//             String command = scanner.next();
//             if (command.equals("Insert")) {
//                 int x = scanner.nextInt();
//                 int y = scanner.nextInt();
//                 L.add(x, y);
//             } else if (command.equals("Delete")) {
//                 int x = scanner.nextInt();
//                 L.remove(x);
//             }
//         }
        
//         // Print the modified list
//         for (int num : L) {
//             System.out.print(num + " ");
//         }
//         scanner.close();
//     }
// }





// // Sometimes it's better to use dynamic size arrays. Java's Arraylist can provide you this feature. Try to solve this problem using Arraylist.
// // You are given n lines. In each line there are zero or more integers. You need to answer a few queries where you need to tell the number located in yth position of xth line.
// // Take your input from System.in.

// // Input Format
// // The first line has an integer n. In each of the next n lines there will be an integer d denoting number of integers on that line and then there will be d space-separated integers. In the next line there will be an integer q denoting number of queries. Each query will consist of two integers x and y.

// // Constraints
// // 1<=n<=20000
// // 0<=d<=50000
// // 1<=q<=1000
// // 1<=x<=n

// // Each number will fit in signed integer.
// // Total number of integers in n lines will not cross 10^5.

// // Output Format
// // In each line, output the number located in yth position of  xth line. If there is no such position, just print "ERROR!"

// // Sample Input
// // 5
// // 5 41 77 74 22 44
// // 1 12
// // 4 37 34 36 52
// // 0
// // 3 20 22 33
// // 5
// // 1 3
// // 3 4
// // 3 1
// // 4 3
// // 5 5

// // Sample Output
// // 74
// // 52
// // 37
// // ERROR!
// // ERROR!



// import java.io.*;
// import java.util.*;
// import java.text.*;
// import java.math.*;
// import java.util.regex.*;

// public class Solution {
//     public static void main(String[] args) throws IOException {
//         // Initialize Scanner to read from standard input
//         Scanner scanner = new Scanner(System.in);

//         // Read number of lines
//         int n = scanner.nextInt();
//         scanner.nextLine(); // consume the newline character

//         // List to store each line of integers as ArrayList
//         List<List<Integer>> lines = new ArrayList<>();

//         // Read each line of integers
//         for (int i = 0; i < n; i++) {
//             // Read the whole line
//             String line = scanner.nextLine();
//             // Create a Scanner to parse the line
//             Scanner lineScanner = new Scanner(line);
//             // First number is the count of integers in the line
//             int d = lineScanner.nextInt();
//             // List to store the integers in this line
//             List<Integer> currentLine = new ArrayList<>();
//             // Add the integers to the currentLine list
//             for (int j = 0; j < d; j++) {
//                 if (lineScanner.hasNextInt()) {
//                     currentLine.add(lineScanner.nextInt());
//                 }
//             }
//             // Add the currentLine list to the lines list
//             lines.add(currentLine);
//             lineScanner.close();
//         }

//         // Read number of queries
//         int q = scanner.nextInt();

//         // Process each query
//         for (int i = 0; i < q; i++) {
//             int x = scanner.nextInt();
//             int y = scanner.nextInt();
//             // Check if the xth line and yth position are valid
//             if (x > 0 && x <= lines.size() && y > 0 && y <= lines.get(x - 1).size()) {
//                 // Output the value at the specified position
//                 System.out.println(lines.get(x - 1).get(y - 1));
//             } else {
//                 // Output "ERROR!" if the position is invalid
//                 System.out.println("ERROR!");
//             }
//         }
        
//         scanner.close();
//     }
// }





// // Let's play a game on an array! You're standing at index 0 of an n-element array named game. From some index i (where 0<=i<n), you can perform one of the following moves:
// // Move Backward: If cell i-1 exists and contains a , you can walk back to cell i-1.
// // Move Forward:
// // If cell i+1 contains a zero, you can walk to cell i+1.
// // If cell i+leap contains a zero, you can jump to cell i+leap.
// // If you're standing in cell n-1 or the value of i+leap>=n, you can walk or jump off the end of the array and win the game.
// // In other words, you can move from index i to index i+1, i-1, or i+leap as long as the destination index is a cell containing  a 0. If the destination index is greater than n-1, you win the game.

// // Function Description
// // Complete the canWin function in the editor below.

// // canWin has the following parameters:

// // int leap: the size of the leap
// // int game[n]: the array to traverse

// // Returns
// // boolean: true if the game can be won, otherwise false

// // Input Format
// // The first line contains an integer,q , denoting the number of queries (i.e., function calls).
// // The 2.q subsequent lines describe each query over two lines:

// // The first line contains two space-separated integers describing the respective values of n and leap.
// // The second line contains n space-separated binary integers (i.e., zeroes and ones) describing the respective values of game0, game1, ....., gamen-1.

// // Constraints
// // 1<=q<=5000
// // 2<=n<=100
// // 0<=leap<=100
// // It is guaranteed that the value of game[0] is always 0.

// // Sample Input
// // STDIN           Function
// // -----           --------
// // 4               q = 4 (number of queries)
// // 5 3             game[] size n = 5, leap = 3 (first query)
// // 0 0 0 0 0       game = [0, 0, 0, 0, 0]
// // 6 5             game[] size n = 6, leap = 5 (second query)
// // 0 0 0 1 1 1     . . .
// // 6 3
// // 0 0 1 1 1 0
// // 3 1
// // 0 1 0

// // Sample Output
// // YES
// // YES
// // NO
// // NO





// import java.util.Scanner;

// public class Solution {

//     public static boolean canWin(int leap, int[] game) {
//         return canWin(leap, game, 0);
//     }

//     private static boolean canWin(int leap, int[] game, int i) {
//         // Base cases
//         if (i >= game.length) {
//             return true;  // If we've reached or passed the end of the array
//         }
//         if (i < 0 || game[i] == 1) {
//             return false;  // If out of bounds or on a cell with a 1
//         }

//         // Mark this cell as visited
//         game[i] = 1;

//         // Explore the three possible moves
//         boolean moveForward = canWin(leap, game, i + 1);
//         boolean jump = canWin(leap, game, i + leap);
//         boolean moveBackward = canWin(leap, game, i - 1);

//         return moveForward || jump || moveBackward;
//     }

//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);
//         int q = scanner.nextInt();

//         for (int i = 0; i < q; i++) {
//             int n = scanner.nextInt();
//             int leap = scanner.nextInt();

//             int[] game = new int[n];
//             for (int j = 0; j < n; j++) {
//                 game[j] = scanner.nextInt();
//             }

//             System.out.println((canWin(leap, game)) ? "YES" : "NO");
//         }
//         scanner.close();
//     }
// }







// // You are given a phone book that consists of people's names and their phone number. After that you will be given some person's name as query. For each query, print the phone number of that person.

// // Input Format
// // The first line will have an integer n denoting the number of entries in the phone book. Each entry consists of two lines: a name and the corresponding phone number.
// // After these, there will be some queries. Each query will contain a person's name. Read the queries until end-of-file.

// // Constraints:
// // A person's name consists of only lower-case English letters and it may be in the format 'first-name last-name' or in the format 'first-name'. Each phone number has exactly 8 digits without any leading zeros.
// // 1<=n<=100000
// // 1<=Query<=100000

// // Output Format
// // For each case, print "Not found" if the person has no entry in the phone book. Otherwise, print the person's name and phone number. See sample output for the exact format.
// // To make the problem easier, we provided a portion of the code in the editor. You can either complete that code or write completely on your own.

// // Sample Input
// // 3
// // uncle sam
// // 99912222
// // tom
// // 11122222
// // harry
// // 12299933
// // uncle sam
// // uncle tom
// // harry

// // Sample Output
// // uncle sam=99912222
// // Not found
// // harry=12299933




// import java.util.*;
// import java.io.*;

// public class Solution {
//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);
//         Map<String, String> phoneBook = new HashMap<>();
        
//         // Read number of entries in the phone book
//         int n = scanner.nextInt();
//         scanner.nextLine(); // Consume the remaining newline character
        
//         // Read the entries and store them in the phone book
//         for (int i = 0; i < n; i++) {
//             String name = scanner.nextLine();
//             String phoneNumber = scanner.nextLine();
//             phoneBook.put(name, phoneNumber);
//         }
        
//         // Read queries until end-of-file and output results
//         while (scanner.hasNextLine()) {
//             String query = scanner.nextLine();
//             if (phoneBook.containsKey(query)) {
//                 System.out.println(query + "=" + phoneBook.get(query));
//             } else {
//                 System.out.println("Not found");
//             }
//         }
        
//         scanner.close();
//     }
// }





// // In computer science, a stack or LIFO (last in, first out) is an abstract data type that serves as a collection of elements, with two principal operations: push, which adds an element to the collection, and pop, which removes the last element that was added.(Wikipedia)
// // A string containing only parentheses is balanced if the following is true: 1. if it is an empty string 2. if A and B are correct, AB is correct, 3. if A is correct, (A) and {A} and [A] are also correct.

// // Examples of some correctly balanced strings are: "{}()", "[{()}]", "({()})"
// // Examples of some unbalanced strings are: "{}(", "({)}", "[[", "}{" etc.
// // Given a string, determine if it is balanced or not.

// // Input Format
// // There will be multiple lines in the input file, each having a single non-empty string. You should read input till end-of-file.
// // The part of the code that handles input operation is already provided in the editor.

// // Output Format
// // For each case, print 'true' if the string is balanced, 'false' otherwise.

// // Sample Input
// // {}()
// // ({()})
// // {}(
// // []

// // Sample Output
// // true
// // true
// // false
// // true



// import java.util.*;
// import java.io.*;

// public class Solution {
//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);

//         // Process each line of input
//         while (scanner.hasNextLine()) {
//             String input = scanner.nextLine();
//             System.out.println(isBalanced(input));
//         }
        
//         scanner.close();
//     }

//     public static boolean isBalanced(String str) {
//         Stack<Character> stack = new Stack<>();

//         for (char ch : str.toCharArray()) {
//             if (ch == '{' || ch == '[' || ch == '(') {
//                 stack.push(ch);
//             } else if (ch == '}' || ch == ']' || ch == ')') {
//                 if (stack.isEmpty()) {
//                     return false;
//                 }
//                 char top = stack.pop();
//                 if ((ch == '}' && top != '{') || 
//                     (ch == ']' && top != '[') || 
//                     (ch == ')' && top != '(')) {
//                     return false;
//                 }
//             }
//         }

//         return stack.isEmpty();
//     }
// }






// // You are given a list of student information: ID, FirstName, and CGPA. Your task is to rearrange them according to their CGPA in decreasing order.
// // If two student have the same CGPA, then arrange them according to their first name in alphabetical order. If those two students also have the same first name, then order them according to their ID. No two students have the same ID.
// // Hint: You can use comparators to sort a list of objects. See the oracle docs to learn about comparators.

// // Input Format
// // The first line of input contains an integer N, representing the total number of students. The next N lines contains a list of student information in the following structure:
// // ID Name CGPA

// // Constraints
// // 2<=N<=1000
// // 0<=ID<=100000
// // 5<=|Name|<=30
// // 0<=CGPA<=4.00


// // The name contains only lowercase English letters. The  IDcontains only integer numbers without leading zeros. The CGPA will contain, at most, 2 digits after the decimal point.

// // Output Format
// // After rearranging the students according to the above rules, print the first name of each student on a separate line.

// // Sample Input
// // 5
// // 33 Rumpa 3.68
// // 85 Ashis 3.85
// // 56 Samiha 3.75
// // 19 Samara 3.75
// // 22 Fahim 3.76

// // Sample Output
// // Ashis
// // Fahim
// // Samara
// // Samiha
// // Rumpa




// import java.util.*;

// class Student {
//     private int id;
//     private String fname;
//     private double cgpa;

//     public Student(int id, String fname, double cgpa) {
//         this.id = id;
//         this.fname = fname;
//         this.cgpa = cgpa;
//     }

//     public int getId() {
//         return id;
//     }

//     public String getFname() {
//         return fname;
//     }

//     public double getCgpa() {
//         return cgpa;
//     }
// }

// public class Solution {
//     public static void main(String[] args) {
//         Scanner in = new Scanner(System.in);
//         int testCases = Integer.parseInt(in.nextLine());

//         List<Student> studentList = new ArrayList<Student>();
//         while (testCases > 0) {
//             int id = in.nextInt();
//             String fname = in.next();
//             double cgpa = in.nextDouble();

//             Student st = new Student(id, fname, cgpa);
//             studentList.add(st);

//             testCases--;
//         }

//         Collections.sort(studentList, new Comparator<Student>() {
//             @Override
//             public int compare(Student s1, Student s2) {
//                 if (s1.getCgpa() != s2.getCgpa()) {
//                     return Double.compare(s2.getCgpa(), s1.getCgpa()); // descending order of CGPA
//                 } else if (!s1.getFname().equals(s2.getFname())) {
//                     return s1.getFname().compareTo(s2.getFname()); // ascending order of names
//                 } else {
//                     return Integer.compare(s1.getId(), s2.getId()); // ascending order of IDs
//                 }
//             }
//         });

//         for (Student st : studentList) {
//             System.out.println(st.getFname());
//         }
//     }
// }






// // In computer science, a double-ended queue (dequeue, often abbreviated to deque, pronounced deck) is an abstract data type that generalizes a queue, for which elements can be added to or removed from either the front (head) or back (tail).
// // Deque interfaces can be implemented using various types of collections such as LinkedList or ArrayDeque classes. For example, deque can be declared as:

// // Deque deque = new LinkedList<>();
// // or
// // Deque deque = new ArrayDeque<>();
// // You can find more details about Deque here.

// // In this problem, you are given N integers. You need to find the maximum number of unique integers among all the possible contiguous subarrays of size M.
// // Note: Time limit is 3 second for this problem.

// // Input Format
// // The first line of input contains two integers N and M: representing the total number of integers and the size of the subarray, respectively. The next line contains N space separated integers.

// // Constraints
// // 1<=N<=100000
// // 1<=M<=100000
// // M<=N

// // The numbers in the array will range between [0, 10000000].

// // Output Format
// // Print the maximum number of unique integers among all possible contiguous subarrays of size M.

// // Sample Input
// // 6 3
// // 5 3 5 2 3 2

// // Sample Output
// // 3

// // Explanation
// // In the sample testcase, there are 4 subarrays of contiguous numbers.

// // s1 = (5,3,5) - Has 2 unique numbers.
// // s2 = (3,5,2)- Has 3 unique numbers.
// // s3 = (5,2,3)- Has 3 unique numbers.
// // s4= (2,3,2) - Has 2 unique numbers.

// // In these subarrays, there are 2,3,3,2 unique numbers, respectively. The maximum amount of unique numbers among all possible contiguous subarrays is 3.



// import java.util.*;

// public class Solution {
//     public static void main(String[] args) {
//         Scanner in = new Scanner(System.in);
//         Deque<Integer> deque = new ArrayDeque<>();
//         HashMap<Integer, Integer> countMap = new HashMap<>();
//         int n = in.nextInt();
//         int m = in.nextInt();

//         int maxUnique = 0;

//         for (int i = 0; i < n; i++) {
//             int num = in.nextInt();
//             deque.addLast(num);

//             if (countMap.containsKey(num)) {
//                 countMap.put(num, countMap.get(num) + 1);
//             } else {
//                 countMap.put(num, 1);
//             }

//             // Maintain the window size of 'm'
//             if (deque.size() > m) {
//                 int removed = deque.removeFirst();
//                 if (countMap.get(removed) == 1) {
//                     countMap.remove(removed);
//                 } else {
//                     countMap.put(removed, countMap.get(removed) - 1);
//                 }
//             }

//             // Update the maximum number of unique elements
//             if (deque.size() == m) {
//                 maxUnique = Math.max(maxUnique, countMap.size());
//             }
//         }

//         System.out.println(maxUnique);
//     }
// }







// // In computer science, a set is an abstract data type that can store certain values, without any particular order, and no repeated values(Wikipedia). 
// // {1,2,3}  is an example of a set, but {1,2,3}  is not a set. Today you will learn how to use sets in java by solving this problem.
// // You are given  pairs of strings. Two pairs (a,b) and (c,d) are identical if a=c and b=d. That also implies (a,b) is not same as (b,a).
// // After taking each pair as input, you need to print number of unique pairs you currently have.
// // Complete the code in the editor to solve this problem.

// // Input Format
// // In the first line, there will be an integer T denoting number of pairs. Each of the next T lines will contain two strings seperated by a single space.

// // Constraints:
// // 1<=T<=100000

// // Length of each string is atmost 5 and will consist lower case letters only.

// // Output Format
// // Print T lines. In the ith line, print number of unique pairs you have after taking i^th pair as input.

// // Sample Input
// // 5
// // john tom
// // john mary
// // john tom
// // mary anna
// // mary anna

// // Sample Output
// // 1
// // 2
// // 2
// // 3
// // 3

// // Explanation
// // After taking the first input, you have only one pair: (john,tom)
// // After taking the second input, you have two pairs: (john, tom) and (john, mary)
// // After taking the third input, you still have two unique pairs.
// // After taking the fourth input, you have three unique pairs: (john,tom), (john, mary) and (mary, anna)
// // After taking the fifth input, you still have three unique pairs.




// import java.io.*;
// import java.util.*;
// import java.text.*;
// import java.math.*;
// import java.util.regex.*;

// public class Solution {

//  public static void main(String[] args) {
//         Scanner s = new Scanner(System.in);
//         int t = s.nextInt();
//         String [] pair_left = new String[t];
//         String [] pair_right = new String[t];
        
//         for (int i = 0; i < t; i++) {
//             pair_left[i] = s.next();
//             pair_right[i] = s.next();
//         }
//         // Create a HashSet to store unique pairs
//         HashSet<String> uniquePairs = new HashSet<>();
        
//         for (int i = 0; i < t; i++) {
//             // Create a string representation of the pair
//             String pair = pair_left[i] + " " + pair_right[i];
            
//             // Add the pair to the set
//             uniquePairs.add(pair);
            
//             // Print the size of the set, which is the number of unique pairs so far
//             System.out.println(uniquePairs.size());
//         }
        
//         s.close();

//     }
// }









// // Generic methods are a very efficient way to handle multiple datatypes using a single method. This problem will test your knowledge on Java Generic methods.
// // Let's say you have an integer array and a string array. You have to write a single method printArray that can print all the elements of both arrays.
// // The method should be able to accept both integer arrays or string arrays.

// // You are given code in the editor. Complete the code so that it prints the following lines:

// // 1
// // 2
// // 3
// // Hello
// // World
// // Do not use method overloading because your answer will not be accepted.





// import java.io.IOException;
// import java.lang.reflect.Method;

// class Printer
// {
//     // Define the generic method
//     public <T> void printArray(T[] array) {
//         for (T element : array) {
//             System.out.println(element);
//         }
//     }
 
// }

// public class Solution {


//     public static void main( String args[] ) {
//         Printer myPrinter = new Printer();
//         Integer[] intArray = { 1, 2, 3 };
//         String[] stringArray = {"Hello", "World"};
//         myPrinter.printArray(intArray);
//         myPrinter.printArray(stringArray);
//         int count = 0;

//         for (Method method : Printer.class.getDeclaredMethods()) {
//             String name = method.getName();

//             if(name.equals("printArray"))
//                 count++;
//         }

//         if(count > 1)System.out.println("Method overloading is not allowed!");
      
//     }
// }





// // Comparators are used to compare two objects. In this challenge, you'll create a comparator and use it to sort an array.
// // The Player class is provided for you in your editor. It has  2 fields: a name String and a score integer.
// // Given an array of n Player objects, write a comparator that sorts them in order of decreasing score; if 2 or more players have the same score, sort those players alphabetically by name. To do this, you must create a Checker class that implements the Comparator interface, then write an int compare(Player a, Player b) method implementing the Comparator.compare(T o1, T o2) method.

// // Input Format
// // Input from stdin is handled by the locked stub code in the Solution class.
// // The first line contains an integer, n, denoting the number of players.
// // Each of the  subsequent lines contains a player's  and , respectively.

// // Constraints
// // 0<=score<=1000
// // 2 players can have the same name.
// // Player names consist of lowercase English letters.

// // Output Format
// // You are not responsible for printing any output to stdout. The locked stub code in Solution will create a Checker object, use it to sort the Player array, and print each sorted element.

// // Sample Input
// // 5
// // amy 100
// // david 100
// // heraldo 50
// // aakansha 75
// // aleksa 150

// // Sample Output
// // aleksa 150
// // amy 100
// // david 100
// // aakansha 75
// // heraldo 50



// import java.util.*;

// // Checker class implementing Comparator<Player>
// class Checker implements Comparator<Player> {
//     public int compare(Player a, Player b) {
//         if (a.score != b.score) {
//             return b.score - a.score; // descending order by score
//         } else {
//             return a.name.compareTo(b.name); // alphabetical order by name
//         }
//     }
// }
// class Player{
//     String name;
//     int score;
    
//     Player(String name, int score){
//         this.name = name;
//         this.score = score;
//     }
// }

// class Solution {

//     public static void main(String[] args) {
//         Scanner scan = new Scanner(System.in);
//         int n = scan.nextInt();

//         Player[] player = new Player[n];
//         Checker checker = new Checker();
        
//         for(int i = 0; i < n; i++){
//             player[i] = new Player(scan.next(), scan.nextInt());
//         }
//         scan.close();
     
//         Arrays.sort(player, checker);
//         for(int i = 0; i < player.length; i++){
//             System.out.printf("%s %s\n", player[i].name, player[i].score);
//         }
//     }
// }




