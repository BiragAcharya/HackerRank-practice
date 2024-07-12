// public class Java_OOP



// // Using inheritance, one class can acquire the properties of others. Consider the following Animal class:

// // class Animal{
// //     void walk(){
// //         System.out.println("I am walking");
// //     }
// // }
// // This class has only one method, walk. Next, we want to create a Bird class that also has a fly method. We do this using extends keyword:

// // class Bird extends Animal {
// //     void fly() {
// //         System.out.println("I am flying");
// //     }
// // }
// // Finally, we can create a Bird object that can both fly and walk.

// // public class Solution{
// //    public static void main(String[] args){

// //       Bird bird = new Bird();
// //       bird.walk();
// //       bird.fly();
// //    }
// // }
// // The above code will print:

// // I am walking
// // I am flying
// // This means that a Bird object has all the properties that an Animal object has, as well as some additional unique properties.

// // The code above is provided for you in your editor. You must add a sing method to the Bird class, then modify the main method accordingly so that the code prints the following lines:

// // I am walking
// // I am flying
// // I am singing


// import java.io.*;
// import java.util.*;
// import java.text.*;
// import java.math.*;
// import java.util.regex.*;

// class Animal{
// 	void walk(){
// 		System.out.println("I am walking");
// 	}
// }

// class Bird extends Animal{
// 	void fly(){
// 		System.out.println("I am flying");
// 	}
    
//     void sing(){
//     System.out.println("I am singing");
//     } 
// }

// public class Solution{

//    public static void main(String args[]){

// 	  Bird bird = new Bird();
// 	  bird.walk();
// 	  bird.fly();
//       bird.sing();
	
//    }
// }




// // Write the following code in your editor below:

// // 1. A class named Arithmetic with a method named add that takes 2 integers as parameters and returns an integer denoting their sum.
// // 2. A class named Adder that inherits from a superclass named Arithmetic.
// // Your classes should not be be public.

// // Input Format
// // You are not responsible for reading any input from stdin; a locked code stub will test your submission by calling the add method on an Adder object and passing it 2 integer parameters.

// // Output Format
// // You are not responsible for printing anything to stdout. Your add method must return the sum of its parameters.

// // Sample Output
// // The main method in the Solution class above should print the following:

// // My superclass is: Arithmetic
// // 42 13 20


// import java.io.*;
// import java.util.*;
// import java.text.*;
// import java.math.*;
// import java.util.regex.*;

// class Arithmetic {
//     int add(int a, int b) {
//         return a + b;
//     }
// }

// class Adder extends Arithmetic {
// }

// public class Solution{
//     public static void main(String []args){
//         // Create a new Adder object
//         Adder a = new Adder();
        
//         // Print the name of the superclass on a new line
//         System.out.println("My superclass is: " + a.getClass().getSuperclass().getName());	
        
//         // Print the result of 3 calls to Adder's `add(int,int)` method as 3 space-separated integers:
//         System.out.print(a.add(10,32) + " " + a.add(10,3) + " " + a.add(10,10) + "\n");
//      }
// }




// // A Java abstract class is a class that can't be instantiated. That means you cannot create new instances of an abstract class.
// //  It works as a base for subclasses. You should learn about Java Inheritance before attempting this challenge.

// // Following is an example of abstract class:

// // abstract class Book{
// //     String title;
// //     abstract void setTitle(String s);
// //     String getTitle(){
// //         return title;
// //     }
// // }
// // If you try to create an instance of this class like the following line you will get an error:

// // Book new_novel=new Book(); 
// // You have to create another class that extends the abstract class. Then you can create an instance of the new class.

// // Notice that setTitle method is abstract too and has no body. That means you must implement the body of that method in the child class.

// // In the editor, we have provided the abstract Book class and a Main class. In the Main class, we created an instance of a class called MyBook. Your task is to write just the MyBook class.

// // Your class mustn't be public.

// // Sample Input
// // A tale of two cities

// // Sample Output
// // The title is: A tale of two cities


// import java.util.*;
// abstract class Book{
// 	String title;
// 	abstract void setTitle(String s);
// 	String getTitle(){
// 		return title;
// 	}
// }

// class MyBook extends Book {
//     @Override
//     void setTitle(String s) {
//         this.title = s;
//     }
// }

// public class Main{
	
// 	public static void main(String []args){
// 		//Book new_novel=new Book(); This line prHMain.java:25: error: Book is abstract; cannot be instantiated
// 		Scanner sc=new Scanner(System.in);
// 		String title=sc.nextLine();
// 		MyBook new_novel=new MyBook();
// 		new_novel.setTitle(title);
// 		System.out.println("The title is: "+new_novel.getTitle());
//       	sc.close();
		
// 	}
// }




