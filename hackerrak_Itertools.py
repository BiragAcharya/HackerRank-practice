




from itertools import product

# Reading the input lists
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))

# Calculating the Cartesian product
cartesian_product = list(product(A, B))

# Printing the output in the required format
print(' '.join(map(str, cartesian_product)))
