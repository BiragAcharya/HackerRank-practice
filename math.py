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



