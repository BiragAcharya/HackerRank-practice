# # Task
# # Given an integer,perform the following conditional actions:

# # If  is odd, print Weird
# # If  is even and in the inclusive range of  to , print Not Weird
# # If  is even and in the inclusive range of  to , print Weird
# # If  is even and greater than , print Not Weird


# n = int(input("Enter number: ").strip())
# if n % 2 != 0:
#     print("Weird")
# else:
#     if 2<= n <= 5:
#         print("Not Weird")
#     elif 6<= n <=20:
#         print("Weird")
#     else:
#         print("Not Weird")



# # Task
# # The provided code stub reads two integers from STDIN, a and b .  Add code to print three lines where:

# # The first line contains the sum of the two numbers.
# # The second line contains the difference of the two numbers (first - second).
# # The third line contains the product of the two numbers.



# a = int(input("Enter first number:").strip())
# b = int(input("Enter second number:").strip())

# sum = a+b
# difference = a-b
# product= a*b
    
# print(sum)
# print(difference)
# print(product)

# # Here is a sample line of code that can be executed in Python:
# # print("Hello, World!") 

# a = "Hello, World!"
# print(a)





# # Task
# # The provided code stub reads two integers, a and b, from STDIN.
# # Add logic to print two lines. The first line should contain the result of integer division,  a//b . The second line should contain the result of float division,  a/b .
# # No rounding or formatting is necessary.

# # Example, a=3 b=5

# # The result of the integer division 3//5 = 0.
# # The result of the float division is 3/5 = 0.6.

# if __name__ == '__main__':
#     a = int(input("Enter a: "))
#     b = int(input("Enter b: "))
    
#     x= a//b
#     y=a/b
    
#     print(x)
#     print(y)




# # Task
# # The provided code stub reads and integer, n, from STDIN. For all non-negative integers i < n, print i^2.

# # Example: n =3
# # The list of non-negative integers that are less than n=3 is [0,1,2]. Print the square of each number on a separate line.

# if __name__ == '__main__':
#     n = int(input("Enter: ").strip())
    
#     for i in range(n):
#         print(i*i)





# # An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

# # In the Gregorian calendar, three conditions are used to identify leap years:

# # The year can be evenly divided by 4, is a leap year, unless:
# # The year can be evenly divided by 100, it is NOT a leap year, unless:
# # The year is also evenly divisible by 400. Then it is a leap year.
# # This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source

# # Task
# # Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
# # Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

# def is_leap(year):
#     leap = False
    
#     if year % 4 ==0:
#         if year % 100 ==0:
#             if year % 400 ==0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
    
#     return leap

# year = int(input("Enter: ").strip())
# print(is_leap(year))


# # The included code stub will read an integer,n , from STDIN.
# # Without using any string methods, try to print the following: 123...n

# # Note that "..." represents the consecutive values in between.
# # Example n=5

# # Print the string 12345.

# # Input Format
# # The first line contains an integer n.

if __name__ == '__main__':
    n = int(input("Enter: "))
    
    for i in range(1, n+1):
        print(i, end='')
