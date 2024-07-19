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

