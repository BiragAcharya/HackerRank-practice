# # Task
# # You are given a two lists A and B. Your task is to compute their cartesian product A X B.

# # Example
# # A = [1, 2]
# # B = [3, 4]

# # AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
# # Note: A and B are sorted lists, and the cartesian product's tuples should be output in sorted order.

# # Input Format
# # The first line contains the space separated elements of list A.
# # The second line contains the space separated elements of list B.

# # Both lists have no duplicate integer elements.

# # Constraints
# # 0<A<30
# # 0<B<30

# # Output Format
# # Output the space separated tuples of the cartesian product.

# # Sample Input
# #  1 2
# #  3 4

# # Sample Output
# #  (1, 3) (1, 4) (2, 3) (2, 4)




# from itertools import product

# # Reading the input lists
# A = list(map(int, input().strip().split()))
# B = list(map(int, input().strip().split()))

# # Calculating the Cartesian product
# cartesian_product = list(product(A, B))

# # Printing the output in the required format
# print(' '.join(map(str, cartesian_product)))







# # Task
# # You are given a string S.
# # Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

# # Input Format
# # A single line containing the space separated string S and the integer value k.

# # Constraints
# # 0<k<=len(S)

# # The string contains only UPPERCASE characters.

# # Output Format
# # Print the permutations of the string S on separate lines.

# # Sample Input
# # HACK 2

# # Sample Output
# # AC
# # AH
# # AK
# # CA
# # CH
# # CK
# # HA
# # HC
# # HK
# # KA
# # KC
# # KH

# # Explanation
# # All possible size 2 permutations of the string "HACK" are printed in lexicographic sorted order.




# from itertools import permutations

# # Reading the input
# input_data = input().strip().split()
# S = input_data[0]
# k = int(input_data[1])

# # Generate permutations of size k
# perms = list(permutations(S, k))

# # Sort permutations lexicographically
# sorted_perms = sorted(perms)

# # Print each permutation on a new line
# for perm in sorted_perms:
#     print(''.join(perm))

