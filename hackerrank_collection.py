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







# # Task
# # You are the manager of a supermarket.
# # You have a list of N items together with their prices that consumers bought on a particular day.
# # Your task is to print each item_name and net_price in order of its first occurrence.

# # item_name = Name of the item.
# # net_price = Quantity of the item sold multiplied by the price of each item.

# # Input Format
# # The first line contains the number of items,N .
# # The next N lines contains the item's name and price, separated by a space.

# # Constraints
# # 0<N<=100

# # Output Format
# # Print the item_name and net_price in order of its first occurrence.

# # Sample Input
# # 9
# # BANANA FRIES 12
# # POTATO CHIPS 30
# # APPLE JUICE 10
# # CANDY 5
# # APPLE JUICE 10
# # CANDY 5
# # CANDY 5
# # CANDY 5
# # POTATO CHIPS 30

# # Sample Output
# # BANANA FRIES 12
# # POTATO CHIPS 60
# # APPLE JUICE 20
# # CANDY 20

# # Explanation
# # BANANA FRIES: Quantity bought: , Price: 12
# # Net Price: 12
# # POTATO CHIPS: Quantity bought: , Price: 30
# # Net Price: 60
# # APPLE JUICE: Quantity bought: , Price: 10
# # Net Price: 20
# # CANDY: Quantity bought: , Price: 5
# # Net Price: 20


# from collections import OrderedDict

# N = int(input())
# items = OrderedDict()

# for _ in range(N):
#     item_name, price = input().rsplit(maxsplit=1)
#     price = int(price)
#     if item_name in items:
#         items[item_name] += price
#     else:
#         items[item_name] = price

# for item_name, net_price in items.items():
#     print(f"{item_name} {net_price}")







# collections.Counter()
# A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

# Sample Code
# >>> from collections import Counter
# >>> 
# >>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# >>> print Counter(myList)
# Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
# >>>
# >>> print Counter(myList).items()
# [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
# >>> 
# >>> print Counter(myList).keys()
# [1, 2, 3, 4, 5]
# >>> 
# >>> print Counter(myList).values()
# [3, 4, 4, 2, 1]

# Task
# Raghu is a shoe shop owner. His shop has X number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.

# Your task is to compute how much money Raghu earned.

# Input Format
# The first line contains X, the number of shoes.
# The second line contains the space separated list of all the shoe sizes in the shop.
# The third line contains N, the number of customers.
# The next N lines contain the space separated values of the shoe size desired by the customer and xi, the price of the shoe.

# Constraints
# 0<X<10^3
# 0<N<10^3
# 20<xi<100
# 2<shoe size<20


# Output Format
# Print the amount of money earned by Raghu.

# Sample Input
# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50

# Sample Output
# 200

# Explanation
# Customer 1: Purchased size 6 shoe for $55.
# Customer 2: Purchased size 6 shoe for $45.
# Customer 3: Size 6 no longer available, so no purchase.
# Customer 4: Purchased size 4 shoe for $40.
# Customer 5: Purchased size 18 shoe for $60.
# Customer 6: Size 10 not available, so no purchase.

# Total money earned = 55+45+40+60=$200 






# from collections import Counter

# # Input the number of shoes
# n = int(input())

# # Input the list of shoe sizes in the shop
# shoe_sizes = list(map(int, input().split()))

# # Create a Counter for shoe sizes
# inventory = Counter(shoe_sizes)

# # Input the number of customers
# m = int(input())

# # Initialize the money earned to 0
# total_earned = 0

# # Process each customer
# for _ in range(m):
#     size, price = map(int, input().split())
    
#     # Check if the desired size is available
#     if inventory[size] > 0:
#         # Add the price to the total earned
#         total_earned += price
#         # Decrease the count of the shoe size in inventory
#         inventory[size] -= 1

# # Output the total money earned
# print(total_earned)





# Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, but did not realize her keyboard's 0 key was broken until after completing the calculation. She wants your help finding the difference between her miscalculation (using salaries with any zeros removed), and the actual average salary.
# Write a query calculating the amount of error (i.e.: actual-miscalculated  average monthly salaries), and round it up to the next integer.

# Input Format
# The EMPLOYEES table is described as follows:

# Note: Salary is per month.

# Constraints
# 1000<Salary<10^5.

# Sample Input


# Sample Output
# 2061


# SELECT CEIL(ABS(
#     (SELECT AVG(CAST(REPLACE(Salary, '0', '') AS UNSIGNED)) FROM EMPLOYEES) - 
#     (SELECT AVG(Salary) FROM EMPLOYEES)
# )) AS ErrorAmount;
