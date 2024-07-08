# # Let's learn about list comprehensions! You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n.
# # Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n.
# # Here, 0<=i<=x ; 0<=j<=y ; 0<=k<=z. Please use list comprehensions rather than multiple loops, as a learning exercise.

# if __name__ == '__main__':
#     x = int(input("Enter x: "))
#     y = int(input("Enter y: "))
#     z = int(input("Enter z: "))
#     n = int(input("Enter n: "))
    
# coordinates = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    
# print(coordinates)




# # Given the participants' score sheet for your University Sports Day, you are required to find the runner-up n score.
# # You are given  scores. Store them in a list and find the score of the runner-up.
# # Input Format
# # The first line contains n. The second line contains an array A[]  of n integers each separated by a space.


# if __name__ == '__main__':
#     n = int(input("Enter n: "))
#     arr = list(map(int, input("Enter array: ").split()))
    
#     # Find the maximum score
#     max_score = max(arr)

#     # Remove all occurrences of the maximum score
#     while max_score in arr:
#         arr.remove(max_score)

#     # Find the runner-up score
#     runner_up_score = max(arr)

#     # Print the runner-up score
#     print(runner_up_score)




# # Given the names and grades for each student in a class of N students,
# # store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# # Note: If there are multiple students with the second lowest grade, order their names alphabetically
# # and print each name on a new line.

# if __name__ == '__main__':
#     students = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         students.append([name, score])
        
# scores = sorted(set([score for name, score in students]))
# second_lowest_score = scores[1]   

# second_lowest_students = [name for name, score in students if score == second_lowest_score]

# second_lowest_students.sort()

# for student in second_lowest_students:
#     print(student)     




# # The provided code stub will read in a dictionary containing key/value pairs of 
# # name:[marks] for a list of students. Print the average of the marks array 
# # for the student name provided, showing 2 places after the decimal.

# # Example marks key: value pairs are 'alpha': [20,30,40]
# # 'beta':[30,50,70]
# # query_name = 'beta'

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
    
#     for _ in range(n):
        
#         entry = input().split()
#         name= entry[0]
#         scores = list(map(float, entry[1:]))
#         student_marks[name] = scores
#     query_name = input()
    
#     query_scores = student_marks[query_name]
#     average_score = sum(query_scores) / len(query_scores)
     
#     print(f"{average_score:.2f}")




# # Consider a list (list = []). You can perform the following commands:
# # insert i e: Insert integer e at position .
# # print: Print the list.
# # remove e: Delete the first occurrence of integer e.
# # append e: Insert integer e at the end of the list.
# # sort: Sort the list.
# # pop: Pop the last element from the list.
# # reverse: Reverse the list.
# # Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above.
# # Iterate through each command in order and perform the corresponding operation on your list.


# if __name__ == '__main__':
#     N = int(input())
#     my_list = []
    
#     for _ in range(N):
#         command = input().strip().split()
#         if command[0] == 'insert':
#             my_list.insert(int(command[1]), int(command[2]))
#         elif command[0] == 'print':
#             print(my_list)
#         elif command[0] == 'remove':
#             my_list.remove(int(command[1]))
#         elif command[0] == 'append':
#             my_list.append(int(command[1]))
#         elif command[0] == 'sort':
#             my_list.sort()
#         elif command[0] == 'pop':
#             my_list.pop()
#         elif command[0] == 'reverse':
#             my_list.reverse()   




# # Task
# # Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of hash(t).
# # Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
# # Input Format
# # The first line contains an integer, n, denoting the number of elements in the tuple.
# # The second line contains n space-separated integers describing the elements in tuple t.


# if __name__ == '__main__':
#     n = int(input("N: "))  # Read the integer n
#     integer_list = map(int, input("iL: ").split())  # Read the space-separated integers and convert them to integers
#     t = tuple(integer_list)  # Create a tuple t from the integers
    
#     result = hash(t)  # Compute the hash value of tuple t
    
#     print(result)  # Print the hash value
