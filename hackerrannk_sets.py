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
