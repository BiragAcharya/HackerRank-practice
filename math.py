# # Task
# # You are given a complex z. Your task is to convert it to polar coordinates.

# # Input Format
# # A single line containing the complex number z. Note: complex() function can be used in python to convert the input as a complex number.

# # Constraints
# # Given number is a valid complex number

# # Output Format
# # Output two lines:
# # The first line should contain the value of .
# # The second line should contain the value of .

# # Sample Input
# #   1+2j

# # Sample Output
# #  2.23606797749979 
# #  1.1071487177940904



# import cmath

# # Input: A complex number z as a string
# z = complex(input().strip())

# # Calculating the magnitude
# r = abs(z)

# # Calculating the angle
# theta = cmath.phase(z)

# # Output the results
# print(r)
# print(theta)




# # You are given a positive integer N. Print a numerical triangle of height N-1 like the one below:
# # 1
# # 22
# # 333
# # 4444
# # 55555
# # ......
# # Can you do it using only arithmetic operations, a single for loop and print statement?

# # Use no more than two lines. The first line (the for statement) is already written for you. You have to complete the print statement.

# # Note: Using anything related to strings will give a score of 0.

# # Input Format
# # A single line containing integer, N.

# # Constraints
# # 1<=N<=9

# # Output Format
# # Print N-1 lines as explained above.

# # Sample Input
# # 5

# # Sample Output
# # 1
# # 22
# # 333
# # 4444




# for i in range(1, int(input())): print(i * (10**i - 1) // 9)

