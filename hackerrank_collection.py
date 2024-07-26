# # Task
# # Dr. John Wesley has a spreadsheet containing a list of student's IDs, marks ,class  and name.
# # Your task is to help Dr. Wesley calculate the average marks of the students.

# # Average = Sum of all marks/TOtal students

# # Note:
# # 1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
# # 2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)

# # Input Format
# # The first line contains an integer N, the total number of students.
# # The second line contains the names of the columns in any order.
# # The next N lines contains the marks, IDs , name  and class, under their respective column names.

# # Constraints
# # 0<N<=100

# # Output Format
# # Print the average marks of the list corrected to 2 decimal places.

# # Sample Input
# # TESTCASE 01
# # 5
# # ID         MARKS      NAME       CLASS     
# # 1          97         Raymond    7         
# # 2          50         Steven     4         
# # 3          91         Adrian     9         
# # 4          72         Stewart    5         
# # 5          80         Peter      6   

# # TESTCASE 02
# # 5

# # MARKS      CLASS      NAME       ID        
# # 92         2          Calum      1         
# # 82         5          Scott      2         
# # 94         2          Jason      3         
# # 55         8          Glenn      4         
# # 82         2          Fergus     5

# # Sample Output
# # TESTCASE 01
# # 78.00

# # TESTCASE 02
# # 81.00

# # Explanation
# # TESTCASE 01
# # Average = (97+50+91+72+80)/5

# # Can you solve this challenge in 4 lines of code or less?
# # NOTE: There is no penalty for solutions that are correct but have more than 4 lines.




# N = int(input())
# columns = input().split()
# marks_idx = columns.index("MARKS")
# print(f"{sum(int(input().split()[marks_idx]) for _ in range(N)) / N:.2f}")







# Task
# You are the manager of a supermarket.
# You have a list of N items together with their prices that consumers bought on a particular day.
# Your task is to print each item_name and net_price in order of its first occurrence.

# item_name = Name of the item.
# net_price = Quantity of the item sold multiplied by the price of each item.

# Input Format
# The first line contains the number of items,N .
# The next N lines contains the item's name and price, separated by a space.

# Constraints
# 0<N<=100

# Output Format
# Print the item_name and net_price in order of its first occurrence.

# Sample Input
# 9
# BANANA FRIES 12
# POTATO CHIPS 30
# APPLE JUICE 10
# CANDY 5
# APPLE JUICE 10
# CANDY 5
# CANDY 5
# CANDY 5
# POTATO CHIPS 30

# Sample Output
# BANANA FRIES 12
# POTATO CHIPS 60
# APPLE JUICE 20
# CANDY 20

# Explanation
# BANANA FRIES: Quantity bought: , Price: 12
# Net Price: 12
# POTATO CHIPS: Quantity bought: , Price: 30
# Net Price: 60
# APPLE JUICE: Quantity bought: , Price: 10
# Net Price: 20
# CANDY: Quantity bought: , Price: 5
# Net Price: 20