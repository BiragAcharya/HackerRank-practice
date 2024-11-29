# # You are given a string and your task is to swap cases. In other words,
# # convert all lowercase letters to uppercase letters and vice versa.

# # For Example:
# # Www.HackerRank.com → wWW.hACKERrANK.COM
# # Pythonist 2 → pYTHONIST 2  
# # Function Description

# # Complete the swap_case function in the editor below. swap_case has the following parameters:
# # string s: the string to modify
# # Returns
# # string: the modified string
# # Input Format
# # A single line containing a string s .


# def swap_case(s):
#     return s.swapcase()

# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)



# # In Python, a string can be split on a delimiter.
# # Example:
# # >>> a = "this is a string"
# # >>> a = a.split(" ") # a is converted to a list of strings. 
# # >>> print a
# # ['this', 'is', 'a', 'string']
# # Joining a string is simple:

# # >>> a = "-".join(a)
# # >>> print a
# # this-is-a-string 



# # Task
# # You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

# # Function Description
# # Complete the split_and_join function in the editor below.
# # split_and_join has the following parameters:
# # string line: a string of space-separated words
# # Returns

# # string: the resulting string
# # Input Format
# # The one line contains a string consisting of space separated words.

# # Sample Input
# # this is a string   
# # Sample Output
# # this-is-a-string


# def split_and_join(line):
#     words = line.split(" ")
#     result = "-".join(words)
#     return result

# if __name__ == '__main__':
#     line = input("Enter value: ")
#     result = split_and_join(line)
#     print(result)



# # You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:
# # Hello firstname lastname! You just delved into python.

# # Function Description
# # Complete the print_full_name function in the editor below.
# # print_full_name has the following parameters:
# # string first: the first name
# # string last: the last name
# # Prints
# # string: 'Hello firstname lastname ! You just delved into python' where firstname and lastname are replaced with first and last.

# # Input Format
# # The first line contains the first name, and the second line contains the last name.

# # Constraints
# # The length of the first and last names are each ≤ 10


# def print_full_name(first, last):
#     print(f"Hello {first} {last}! You just delved into python.")
    
# if __name__ == '__main__':
#     first_name = input("Enter firstname: ")
#     last_name = input("Enter lastname:  ")
#     print_full_name(first_name, last_name)



# # We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

# # Let's try to understand this with an example.
# # You are given an immutable string, and you want to make changes to it.

# # Example
# # >>> string = "abracadabra"
# # You can access an index by:

# # >>> print string[5]
# # a
# # What if you would like to assign a value?

# # >>> string[5] = 'k' 
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# # TypeError: 'str' object does not support item assignment
# # How would you approach this?

# # One solution is to convert the string to a list and then change the value.
# # Example

# # >>> string = "abracadabra"
# # >>> l = list(string)
# # >>> l[5] = 'k'
# # >>> string = ''.join(l)
# # >>> print string
# # abrackdabra\


# def mutate_string(string, position, character):
#     string_list = list(string)
#     string_list[position] = character
#     return ''.join(string_list)

# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)

#     OR

# def mutate_string(string: str, position: int, character: str) -> str:
#     before = string[:position]
#     new_char = character
#     after = string[position + 1:]
#     return before + new_char + after

# if __name__ == '__main__':
#     original_string = input("Enter the original string: ")
#     position = int(input("Enter the position to change (0-based index): "))
#     new_character = input("Enter the new character: ")
    
#     new_string = mutate_string(original_string, position, new_character)
#     print(new_string)



# # In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string.
# #  String traversal will take place from left to right, not from right to left.
# # NOTE: String letters are case-sensitive.

# # Input Format
# # The first line of input contains the original string. The next line contains the substring.
# # Constraints
# # 1<=len(string) <= 200
# # Each character in the string is an ascii character.


# def count_substring(string, sub_string):
#     count = 0
#     sub_len = len(sub_string)
    
#     # Loop through the string
#     for i in range(len(string) - sub_len + 1):
#         # Check if the substring matches the part of the string
#         if string[i:i + sub_len] == sub_string:
#             count += 1
            
#     return count

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)


# # Task

# # You are given a string .
# # Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

# # Input Format
# # A single line containing a string .

# # Constraints
# # 0<len(S) < 100

# # Output Format
# # In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# # In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# # In the third line, print True if  has any digits. Otherwise, print False.
# # In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# # In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

# # Sample Input

# # qA2
# # Sample Output

# # True
# # True
# # True
# # True
# # True




# if __name__ == '__main__':
#     s = input().strip()  # Input the string and strip any extra whitespace
    
#     # Initialize variables to store the results of checks
#     has_alnum = any(c.isalnum() for c in s)
#     has_alpha = any(c.isalpha() for c in s)
#     has_digit = any(c.isdigit() for c in s)
#     has_lower = any(c.islower() for c in s)
#     has_upper = any(c.isupper() for c in s)
    
#     # Print the results as required
#     print(has_alnum)
#     print(has_alpha)
#     print(has_digit)
#     print(has_lower)
#     print(has_upper)



# # You are given a string S and width w.
# # Your task is to wrap the string into a paragraph of width .

# # Function Description
# # Complete the wrap function in the editor below.
# # wrap has the following parameters:

# # string string: a long string
# # int max_width: the width to wrap to
# # Returns

# # string: a single string with newline characters ('\n') where the breaks should be



# import textwrap

# def wrap(string, max_width):
#     wrapped_lines = []
#     for i in range(0, len(string), max_width):
#         wrapped_lines.append(string[i:i + max_width])
#     return '\n'.join(wrapped_lines)


# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)



# # Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# # Mat size must be N X M. (N is an odd natural number, and M is  3 times N.)
# # The design should have 'WELCOME' written in the center.
# # The design pattern should only use |, . and - characters.



# def print_door_mat(N, M):
#     # Top part
#     for i in range(N // 2):
#         pattern = '.|.' * (2 * i + 1)
#         print(pattern.center(M, '-'))
    
#     # Middle part
#     print('WELCOME'.center(M, '-'))
    
#     # Bottom part (same as top part but reversed)
#     for i in range(N // 2 - 1, -1, -1):
#         pattern = '.|.' * (2 * i + 1)
#         print(pattern.center(M, '-'))

# if __name__ == '__main__':
#     N, M = map(int, input().split())
#     print_door_mat(N, M)



# # Given an integer,n , print the following values for each integer i from 1 to n:

# # Decimal
# # Octal
# # Hexadecimal (capitalized)
# # Binary
# # Function Description

# # Complete the print_formatted function in the editor below.

# # print_formatted has the following parameters:

# # int number: the maximum value to print
# # Prints

# # The four values must be printed on a single line in the order specified above for each i from 1 to number.
# #  Each value should be space-padded to match the width of the binary value of  number and
# # the values should be separated by a single space.


# def print_formatted(number):
#     width = len(bin(number)[2:])
    
#     # Iterate from 1 to number
#     for i in range(1, number + 1):
#         decimal_str = format(i, 'd').rjust(width)  # Decimal
#         octal_str = format(i, 'o').rjust(width)    # Octal
#         hex_str = format(i, 'X').rjust(width)      # Capitalized Hexadecimal
#         binary_str = format(i, 'b').rjust(width)   # Binary
        
#         # Print all formatted values in a single line
#         print(f"{decimal_str} {octal_str} {hex_str} {binary_str}")

# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)




# # You are given an integer, . Your task is to print an alphabet rangoli of size . 
# # (Rangoli is a form of Indian folk art based on creation of patterns.)
# # Different sizes of alphabet rangoli are shown below:

# # #size 3
# # ----c----
# # --c-b-c--
# # c-b-a-b-c
# # --c-b-c--
# # ----c----

# # #size 5

# # --------e--------
# # ------e-d-e------
# # ----e-d-c-d-e----
# # --e-d-c-b-c-d-e--
# # e-d-c-b-a-b-c-d-e
# # --e-d-c-b-c-d-e--
# # ----e-d-c-d-e----
# # ------e-d-e------
# # --------e--------

# # #size 10

# # ------------------j------------------
# # ----------------j-i-j----------------
# # --------------j-i-h-i-j--------------
# # ------------j-i-h-g-h-i-j------------
# # ----------j-i-h-g-f-g-h-i-j----------
# # --------j-i-h-g-f-e-f-g-h-i-j--------
# # ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# # ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# # --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# # j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
# # --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# # ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# # ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# # --------j-i-h-g-f-e-f-g-h-i-j--------
# # ----------j-i-h-g-f-g-h-i-j----------
# # ------------j-i-h-g-h-i-j------------
# # --------------j-i-h-i-j--------------
# # ----------------j-i-j----------------
# # ------------------j------------------



# def print_rangoli(size):
#     import string
#     alphabet = string.ascii_lowercase
    
#     # Determine the maximum character
#     max_char = alphabet[size - 1]
    
#     # Build the rangoli
#     lines = []
#     for i in range(size):
#         # Create the sequence of characters
#         line = '-'.join(alphabet[size - 1:i:-1] + alphabet[i:size])
#         lines.append(line.center(4 * size - 3, '-'))
    
#     # Print the rangoli
#     for line in lines[::-1] + lines[1:]:
#         print(line)

# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)





# # Kevin and Stuart want to play the 'The Minion Game'.

# # Game Rules

# # Both players are given the same string, .
# # Both players have to make substrings using the letters of the string .
# # Stuart has to make words starting with consonants.
# # Kevin has to make words starting with vowels.
# # The game ends when both players have made all possible substrings.

# # Scoring
# # A player gets +1 point for each occurrence of the substring in the string .

# # For Example:
# # String  = BANANA
# # Kevin's vowel beginning word = ANA
# # Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
# # For better understanding, see the image below:
# # banana.png
# # Your task is to determine the winner of the game and their score.

# # Function Description
# # Complete the minion_game in the editor below.
# # minion_game has the following parameters:
# # string string: the string to analyze
# # Prints

# # string: the winner's name and score, separated by a space on one line, or Draw if there is no winner


# def minion_game(string):
#     vowels = 'AEIOU'
#     length = len(string)
#     stuart_score = 0
#     kevin_score = 0
    
#     for i in range(length):
#         if string[i] in vowels:
#             kevin_score += (length - i)
#         else:
#             stuart_score += (length - i)
    
#     if stuart_score > kevin_score:
#         print(f"Stuart {stuart_score}")
#     elif kevin_score > stuart_score:
#         print(f"Kevin {kevin_score}")
#     else:
#         print("Draw")

# if __name__ == '__main__':
#     s = input()
#     minion_game(s)








# # You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
# # alison heck => Alison Heck
# # Given a full name, your task is to capitalize the name appropriately.

# # Input Format
# # A single line of input containing the full name, S.

# # Constraints
# # 0<len(S) < 1000

# # The string consists of alphanumeric characters and spaces.
# # Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

# # Output Format
# # Print the capitalized string, S.

# # Sample Input
# # chris alan

# # Sample Output
# # Chris Alan



# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# # Complete the solve function below.
# def solve(s):
#     # Capitalize each word in the string
#     capitalized_string = ' '.join(word.capitalize() for word in s.split(' '))
#     return capitalized_string


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = solve(s)

#     fptr.write(result + '\n')

#     fptr.close()








# # In Python, a string of text can be aligned left, right and center.
# # .ljust(width)

# # This method returns a left aligned string of length width.
# # >>> width = 20
# # >>> print 'HackerRank'.ljust(width,'-')
# # HackerRank----------  
# # .center(width)

# # This method returns a centered string of length width.
# # >>> width = 20
# # >>> print 'HackerRank'.center(width,'-')
# # -----HackerRank-----
# # .rjust(width)

# # This method returns a right aligned string of length width.
# # >>> width = 20
# # >>> print 'HackerRank'.rjust(width,'-')
# # ----------HackerRank

# # Task
# # You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
# # Your task is to replace the blank (______) with rjust, ljust or center.

# # Input Format
# # A single line containing the thickness value for the logo.

# # Constraints
# # The thickness must be an odd number.
# # 0<thickness<50

# # Output Format
# # Output the desired logo.

# # Sample Input
# # 5

# # Sample Output
# #     H    
# #    HHH   
# #   HHHHH  
# #  HHHHHHH 
# # HHHHHHHHH
# #   HHHHH               HHHHH             
# #   HHHHH               HHHHH             
# #   HHHHH               HHHHH             
# #   HHHHH               HHHHH             
# #   HHHHH               HHHHH             
# #   HHHHH               HHHHH             
# #   HHHHHHHHHHHHHHHHHHHHHHHHH   
# #   HHHHHHHHHHHHHHHHHHHHHHHHH   
# #   HHHHHHHHHHHHHHHHHHHHHHHHH   
# #   HHHHH               HHHHH             
# #   HHHHH               HHHHH             
# #   HHHHH               HHHHH             
# #   HHHHH               HHHHH             
# #   HHHHH               HHHHH             
# #   HHHHH               HHHHH             
# #                     HHHHHHHHH 
# #                      HHHHHHH  
# #                       HHHHH   
# #                        HHH    
# #                         H 
# # Language
# # Pypy 3
# # More
# # 1
# # # Enter your code here. Read input from STDIN. Print output to STDOUT
# # Line: 1 Col: 70

# # Test against custom input




# # Enter your code here. Read input from STDIN. Print output to STDOUT
# thickness = int(input()) # This must be an odd number
# c = 'H'

# # Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))

# # Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

# # Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))    

# # Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))    

# # Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
