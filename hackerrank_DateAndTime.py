# # Task
# # You are given a date. Your task is to find what the day is on that date.

# # Input Format
# # A single line of input containing the space separated month, day and year, respectively, in  MM|DD|YYYY  format.

# # Constraints
# # 2000<year<3000

# # Output Format
# # Output the correct day in capital letters.

# # Sample Input
# # 08 05 2015

# # Sample Output
# # WEDNESDAY
# # Explanation

# # The day on August 5th 2015 was WEDNESDAY.


# import datetime

# # Step 1: Read input
# input_str = input()

# # Step 2: Parse the input
# month, day, year = map(int, input_str.split())

# # Step 3: Create a date object
# date = datetime.date(year, month, day)

# # Step 4: Find the day of the week
# day_of_week = date.strftime("%A").upper()

# # Step 5: Print the result
# print(day_of_week)





