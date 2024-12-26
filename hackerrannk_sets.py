# # A set is an unordered collection of elements without duplicate entries.
# # When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.
# # Example
# # >>> print set()
# # set([])

# # >>> print set('HackerRank')
# # set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])

# # >>> print set([1,2,1,2,3,4,5,6,0,9,12,22,3])
# # set([0, 1, 2, 3, 4, 5, 6, 9, 12, 22])

# # >>> print set((1,2,3,4,5,5))
# # set([1, 2, 3, 4, 5])

# # >>> print set(set(['H','a','c','k','e','r','r','a','n','k']))
# # set(['a', 'c', 'r', 'e', 'H', 'k', 'n'])

# # >>> print set({'Hacker' : 'DOSHI', 'Rank' : 616 })
# # set(['Hacker', 'Rank'])

# # >>> print set(enumerate(['H','a','c','k','e','r','r','a','n','k']))
# # set([(6, 'r'), (7, 'a'), (3, 'k'), (4, 'e'), (5, 'r'), (9, 'k'), (2, 'c'), (0, 'H'), (1, 'a'), (8, 'n')])
# # Basically, sets are used for membership testing and eliminating duplicate entries.



# # Task
# # Now, let's use our knowledge of sets and help Mickey.
# # Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.
# # Formula used:
# # Function Description
# # Complete the average function in the editor below.
# # average has the following parameters:
# # int arr: an array of integers

# # Returns
# # float: the resulting float value rounded to 3 places after the decimal

# # Input Format
# # The first line contains the integer,N , the size of arr.
# # The second line contains the N space-separated integers, arr[i].

# # Constraints
# # 0<N<=100


# def average(array):
#    distinct_heights = set(arr)  # Create a set to remove duplicates
#    return round(sum(distinct_heights) / len(distinct_heights), 3)  # Calculate and return the average rounded to 3 decimal places

# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = average(arr)
#     print(result)



# # Task
# # Given 2 sets of integers,M  and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

# # Input Format
# # The first line of input contains an integer,M .
# # The second line contains M space-separated integers.
# # The third line contains an integer, N.
# # The fourth line contains N space-separated integers.

# # Output Format
# # Output the symmetric difference integers in ascending order, one per line.

# # Sample Input
# # STDIN       Function
# # -----       --------
# # 4           set a size M = 4
# # 2 4 5 9     a = {2, 4, 5, 9}
# # 4           set b size N = 4
# # 2 4 11 12   b = {2, 4, 11, 12}

# # Sample Output
# # 5
# # 9
# # 11
# # 12


# if __name__ == '__main__':
#     # Read the size of the first set
#     m = int(input())
#     # Read the elements of the first set
#     a = set(map(int, input().split()))
    
#     # Read the size of the second set
#     n = int(input())
#     # Read the elements of the second set
#     b = set(map(int, input().split()))
    
#     # Compute the symmetric difference
#     symmetric_difference = a.symmetric_difference(b)
    
#     # Sort the symmetric difference
#     sorted_result = sorted(symmetric_difference)
    
#     # Print each element in the sorted result on a new line
#     for element in sorted_result:
#         print(element)



# # Task
# # Now, let's use our knowledge of sets and help Mickey.
# # Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

# # Formula used:
# # Function Description
# # Complete the average function in the editor below.
# # average has the following parameters:

# # int arr: an array of integers
# # Returns

# # float: the resulting float value rounded to 3 places after the decimal
# # Input Format

# # The first line contains the integer, N, the size of arr.
# # The second line contains the N space-separated integers,arr[i] .

# # Constraints
# # 0<N<=100

# # Sample Input
# # STDIN                                       Function
# # -----                                       --------
# # 10                                          arr[] size N = 10
# # 161 182 161 154 176 170 167 171 170 174     arr = [161, 181, ..., 174]

# # Sample Output
# # 169.375


# def average(array):
#    distinct_heights = set(arr)  # Create a set to remove duplicates
#    return round(sum(distinct_heights) / len(distinct_heights), 3)  # Calculate and return the average rounded to 3 decimal places

# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = average(arr)
#     print(result)




# # There is an array of n integers. There are also  disjoint sets,A  and B, each containing m integers.
# # You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0.
# # For each i integer in the array, if i belongs A, you add 1 to your happiness. If i belongs B, you add -1 to your happiness.
# #  Otherwise, your happiness does not change. Output your final happiness at the end.
# # Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.

# # Constraints
# # 1<=n<=10^5
# # 1<=m<=10^5
# # 1<=Any integer in the input <=10^9


# # Input Format
# # The first line contains integers n and m separated by a space.
# # The second line contains n integers, the elements of the array.
# # The third and fourth lines contain m integers, A and B, respectively.

# # Output Format
# # Output a single integer, your total happiness.

# # Sample Input
# # 3 2
# # 1 5 3
# # 3 1
# # 5 7



# def calculate_happiness(arr, A, B):
#     happiness = 0
    
#     # Iterate through each element in the array
#     for i in arr:
#         if i in A:
#             happiness += 1
#         elif i in B:
#             happiness -= 1
    
#     return happiness

# if __name__ == '__main__':
#     # Read the first line of input
#     n, m = map(int, input().split())
    
#     # Read the second line of input as the array
#     arr = list(map(int, input().split()))
    
#     # Read the third and fourth lines as sets A and B
#     A = set(map(int, input().split()))
#     B = set(map(int, input().split()))
    
#     # Calculate the happiness
#     result = calculate_happiness(arr, A, B)
    
#     # Print the result
#     print(result)




# # Task
# # Apply your knowledge of the .add() operation to help your friend Rupal.
# # Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection.
# # She asked for your help. You pick the stamps one by one from a stack of N country stamps.
# # Find the total number of distinct country stamps.

# # Input Format
# # The first line contains an integer N, the total number of country stamps.
# # The next N lines contains the name of the country where the stamp is from.

# # Constraints
# # 0<N<1000

# # Output Format
# # Output the total number of distinct country stamps on a single line.

# # Sample Input
# # 7
# # UK
# # China
# # USA
# # France
# # New Zealand
# # UK
# # France 

# # Sample Output
# # 5

# # Explanation
# # UK and France repeat twice. Hence, the total number of distinct country stamps is 5 (five).


# def count_distinct_stamps(n, countries):
#     country_set = set()
#     for country in countries:
#         country_set.add(country)
#     return len(country_set)

# if __name__ == '__main__':
#     n = int(input())
#     countries = [input().strip() for _ in range(n)]
#     result = count_distinct_stamps(n, countries)
#     print(result)





# # Task
# # Apply your knowledge of the .add() operation to help your friend Rupal.
# # Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection.
# # She asked for your help. You pick the stamps one by one from a stack of N country stamps.
# # Find the total number of distinct country stamps.

# # Input Format
# # The first line contains an integer ,N the total number of country stamps.
# # The next N lines contains the name of the country where the stamp is from.

# # Constraints
# # 0<N<1000

# # Output Format
# # Output the total number of distinct country stamps on a single line.

# # Sample Input
# # 7
# # UK
# # China
# # USA
# # France
# # New Zealand
# # UK
# # France 

# # Sample Output
# # 5
# # Explanation
# # UK and France repeat twice. Hence, the total number of distinct country stamps is  (five).



# def count_distinct_stamps(n, countries):
#     country_set = set()
#     for country in countries:
#         country_set.add(country)
#     return len(country_set)

# if __name__ == '__main__':
#     n = int(input())
#     countries = [input().strip() for _ in range(n)]
#     result = count_distinct_stamps(n, countries)
#     print(result)






# # Task
# # The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.
# # You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.

# # Input Format
# # The first line contains an integer,n , the number of students who have subscribed to the English newspaper.
# # The second line contains n space separated roll numbers of those students.
# # The third line contains b, the number of students who have subscribed to the French newspaper.
# # The fourth line contains b space separated roll numbers of those students.

# # Constraints
# # 0<Total number of students in college < 1000

# # Output Format
# # Output the total number of students who have at least one subscription.

# # Sample Input
# # 9
# # 1 2 3 4 5 6 7 8 9
# # 9
# # 10 1 2 3 11 21 55 6 8

# # Sample Output
# # 13






# def count_unique_subscribers(n, english_roll_numbers, b, french_roll_numbers):
#     # Convert roll numbers to sets
#     english_set = set(english_roll_numbers)
#     french_set = set(french_roll_numbers)
    
#     # Compute the union of both sets
#     unique_subscribers = english_set.union(french_set)
    
#     # Return the number of unique subscribers
#     return len(unique_subscribers)

# if __name__ == '__main__':
#     # Read the number of English subscribers
#     n = int(input())
#     # Read the roll numbers of English subscribers
#     english_roll_numbers = list(map(int, input().split()))
    
#     # Read the number of French subscribers
#     b = int(input())
#     # Read the roll numbers of French subscribers
#     french_roll_numbers = list(map(int, input().split()))
    
#     # Calculate the number of unique subscribers
#     result = count_unique_subscribers(n, english_roll_numbers, b, french_roll_numbers)
#     # Print the result
#     print(result)





# # Task
# # The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.
# # You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to both newspapers.

# # Input Format
# # The first line contains n, the number of students who have subscribed to the English newspaper.
# # The second line contains n space separated roll numbers of those students.
# # The third line contains b, the number of students who have subscribed to the French newspaper.
# # The fourth line contains b space separated roll numbers of those students.

# # Constraints
# # 0<Total number of students in college < 1000

# # Output Format
# # Output the total number of students who have subscriptions to both English and French newspapers.

# # Sample Input
# # 9
# # 1 2 3 4 5 6 7 8 9
# # 9
# # 10 1 2 3 11 21 55 6 8

# # Sample Output
# # 5
# # Explanation
# # The roll numbers of students who have both subscriptions:
# #  and .
# # Hence, the total is  students.



# # Read the number of students subscribed to the English newspaper
# n = int(input())
# # Read the roll numbers of English subscribers
# english_subscribers = set(map(int, input().split()))

# # Read the number of students subscribed to the French newspaper
# b = int(input())
# # Read the roll numbers of French subscribers
# french_subscribers = set(map(int, input().split()))

# # Find the intersection of both sets
# both_subscribers = english_subscribers & french_subscribers

# # Output the total number of students who have subscriptions to both newspapers
# print(len(both_subscribers))






# # Task
# # Students of District College have a subscription to English and French newspapers. Some students have subscribed to only the English newspaper, some have subscribed to only the French newspaper, and some have subscribed to both newspapers.
# # You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to only English newspapers.

# # Input Format
# # The first line contains the number of students who have subscribed to the English newspaper.
# # The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
# # The third line contains the number of students who have subscribed to the French newspaper.
# # The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

# # Constraints
# # 0<Total number of students in college < 1000

# # Output Format
# # Output the total number of students who are subscribed to the English newspaper only.

# # Sample Input
# # 9
# # 1 2 3 4 5 6 7 8 9
# # 9
# # 10 1 2 3 11 21 55 6 8

# # Sample Output
# # 4

# # Explanation
# # The roll numbers of students who only have English newspaper subscriptions are:4,5,7
# #  and 9.
# # Hence, the total is 4 students.



# # Read the number of students subscribed to the English newspaper
# n = int(input())
# # Read the roll numbers of English subscribers
# english_subscribers = set(map(int, input().split()))

# # Read the number of students subscribed to the French newspaper
# b = int(input())
# # Read the roll numbers of French subscribers
# french_subscribers = set(map(int, input().split()))

# # Find the difference between the English and French subscribers sets
# only_english_subscribers = english_subscribers - french_subscribers

# # Output the total number of students who are subscribed to only the English newspaper
# print(len(only_english_subscribers))





# # Task
# # Students of District College have subscriptions to English and French newspapers. Some students have subscribed to English only, some have subscribed to French only, and some have subscribed to both newspapers.
# # You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.

# # Input Format
# # The first line contains the number of students who have subscribed to the English newspaper.
# # The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
# # The third line contains the number of students who have subscribed to the French newspaper.
# # The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

# # Constraints
# # 0<Tot5al number of students in college < 1000

# # Output Format
# # Output total number of students who have subscriptions to the English or the French newspaper but not both.

# # Sample Input
# # 9
# # 1 2 3 4 5 6 7 8 9
# # 9
# # 10 1 2 3 11 21 55 6 8

# # Sample Output
# # 8

# # Explanation
# # The roll numbers of students who have subscriptions to English or French newspapers but not both are: 4,5,7,9,10,11,21
# #  and 55.
# # Hence, the total is 8 students.



# # Read the number of students subscribed to the English newspaper
# n = int(input())
# # Read the roll numbers of English subscribers
# english_subscribers = set(map(int, input().split()))

# # Read the number of students subscribed to the French newspaper
# b = int(input())
# # Read the roll numbers of French subscribers
# french_subscribers = set(map(int, input().split()))

# # Find the symmetric difference between the English and French subscribers sets
# exclusive_subscribers = english_subscribers.symmetric_difference(french_subscribers)

# # Output the total number of students who have subscriptions to the English or the French newspaper but not both
# print(len(exclusive_subscribers))




# # TASK
# # You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.
# # Your task is to execute those operations and print the sum of elements from set A.

# # Input Format
# # The first line contains the number of elements in set A.
# # The second line contains the space separated list of elements in set A.
# # The third line contains integer N, the number of other sets.
# # The next 2*N lines are divided into N parts containing two lines each.
# # The first line of each part contains the space separated entries of the operation name and the length of the other set.

# # The second line of each part contains space separated list of elements in the other set A.
# # 0<len(set(A))<1000
# # 0<len(otherSets)<100
# # 0<N<100

# # Output Format
# # Output the sum of elements in set A.

# # Sample Input
# #  16
# #  1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
# #  4
# #  intersection_update 10
# #  2 3 5 6 8 9 1 4 7 11
# #  update 2
# #  55 66
# #  symmetric_difference_update 5
# #  22 7 35 62 58
# #  difference_update 7
# #  11 22 35 55 58 62 66

# # Sample Output
# # 38




# # Step 1: Read inputs
# num_elements = int(input())
# A = set(map(int, input().split()))
# N = int(input())

# # Step 2: Process each operation
# for _ in range(N):
#     operation = input().split()[0]
#     other_set = set(map(int, input().split()))
    
#     # Perform the appropriate operation on set A
#     if operation == "intersection_update":
#         A.intersection_update(other_set)
#     elif operation == "update":
#         A.update(other_set)
#     elif operation == "symmetric_difference_update":
#         A.symmetric_difference_update(other_set)
#     elif operation == "difference_update":
#         A.difference_update(other_set)

# # Step 3: Output the sum of elements in set A
# print(sum(A))




# # You are given two sets, A and B.
# # Your job is to find whether set A is a subset of set B.

# # If set A is subset of set B, print True.
# # If set A is not a subset of set B, print False.

# # Input Format
# # The first line will contain the number of test cases, T.
# # The first line of each test case contains the number of elements in set A.
# # The second line of each test case contains the space separated elements of set A.
# # The third line of each test case contains the number of elements in set B.
# # The fourth line of each test case contains the space separated elements of set B.

# # Constraints
# # 0<T<21
# # 0<Number of elements in each set < 1001

# # Output Format
# # Output True or False for each test case on separate lines.

# # Sample Input
# # 3
# # 5
# # 1 2 3 5 6
# # 9
# # 9 8 5 6 3 2 1 4 7
# # 1
# # 2
# # 5
# # 3 6 5 4 1
# # 7
# # 1 2 3 5 6 8 9
# # 3
# # 9 8 2

# # Sample Output
# # True 
# # False
# # False

# # Explanation
# # Test Case 01 Explanation
# # Set  A= {1 2 3 5 6}
# # Set  B= {9 8 5 6 3 2 1 4 7}
# # All the elements of set A are elements of set B.
# # Hence, set A is a subset of set B.




# # Number of test cases
# T = int(input())

# # Process each test case
# for _ in range(T):
#     # Read the number of elements in set A and set A itself
#     num_elements_A = int(input())
#     A = set(map(int, input().split()))
    
#     # Read the number of elements in set B and set B itself
#     num_elements_B = int(input())
#     B = set(map(int, input().split()))
    
#     # Check if A is a subset of B and print the result
#     print(A.issubset(B))




# # Task
# # The code in your editor does the following:

# # Reads an integer from stdin and saves it to a variable, n, denoting some number of integers.
# # Reads n integers corresponding to a0,a1,....,an-1 from stdin and saves each integer ai to a variable, val.
# # Attempts to print each element of an array of integers named a.
# # Write the following code in the unlocked portion of your editor:

# # Create an array, a , capable of holding n integers.
# # Modify the code in the loop so that it saves each sequential value to its corresponding location in the array. For example, the first value must be stored in a0, the second value must be stored in a1, and so on.
# # Good luck!

# # Input Format
# # The first line contains a single integer,n , denoting the size of the array.
# # Each line i of the n subsequent lines contains a single integer denoting the value of element ai.

# # Output Format
# # You are not responsible for printing any output to stdout. Locked code in the editor loops through array a and prints each sequential element on a new line.

# # Sample Input
# # 5
# # 10
# # 20
# # 30
# # 40
# # 50

# # Sample Output
# # 10
# # 20
# # 30
# # 40
# # 50

# # Explanation
# # When we save each integer to its corresponding index in a, we get a=[10,20,30,40,50] . The locked code prints each array element on a new line from left to right.





# import java.util.*;

# public class Solution {

#     public static void main(String[] args) {
	   
#         Scanner scan = new Scanner(System.in);
#         int n = scan.nextInt();
#         int[] a = new int[n];
        
#         for (int i = 0; i < n; i++) {
#             a[i] = scan.nextInt();
#         }
        
#         scan.close();

#         // Prints each sequential element in array a
#         for (int i = 0; i < a.length; i++) {
#             System.out.println(a[i]);
#         }
#     }
# }
