# # Task
# # You are given a date.Your task is to find what the day is on that date.
# # Input Format
# # A single line of input containing the space separated month, day and year respectively, in  MM|DD|YYYY  format.

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
# month,day,year = map(int, input_str.split())

# # Step 3: Create a date object
# date = datetime.date(year,month,day)

# # Step 4: Find the day of the week
# day_of_week = date.strftime("%A").upper()

# # Step 5: Print the result
# print(day_of_week)



# # When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed.
# # Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.
# # Since sometimes posts are published and viewed in different time zones, this can be confusing. 
# # You are given two timestamps of one such post that a user can see on his newsfeed in the following format:
# # Day dd Mon yyyy hh:mm:ss +xxxx
# # Here +xxxx represents the time zone.Your task is to print the absolute difference (in seconds) between them.

# # Input Format
# # The first line contains T, the number of testcases.
# # Each testcase contains 2 lines, representing time t1 and time t2.

# # Constraints
# # Input contains only valid timestamps
# # .year <=3000
# # Output Format
# # Print the absolute difference(t1-t2)  in seconds.

# # Sample Input 0
# # 2
# # Sun 10 May 2015 13:54:36 -0700
# # Sun 10 May 2015 13:54:36 -0000
# # Sat 02 May 2015 19:54:36 +0530
# # Fri 01 May 2015 13:54:36 -0000

# # Sample Output 0
# # 25200
# # 88200

# # Explanation 0
# # In the first query, when we compare the time in UTC for both the time stamps, we see a difference of 7 hours. which is  7 * 3600 seconds or 25200 seconds.
# # Similarly, in the second query, time difference is 5 hours and 30 minutes for time zone adjusting for that we have a difference of 1 day and 30 minutes. Or  24 * 3600 + 30 * 60 =88200



# from datetime import datetime
# def parse_timestamp(timestamp):
#     return datetime.strptime(timestamp, "%a %d %b %Y %H:%M:%S %z")

# def calculate_time_difference(t1, t2):
#     time1 = parse_timestamp(t1)
#     time2 = parse_timestamp(t2)
#     return abs(int((time1 - time2).total_seconds()))

# def main():
#     # Read number of test cases
#     T = int(input().strip())
    
#     results = []
#     for _ in range(T):
#         t1 = input().strip()
#         t2 = input().strip()
#         diff = calculate_time_difference(t1, t2)
#         results.append(diff)
    
#     for result in results:
#         print(result)

# if __name__ == "__main__":
#     main()




# # You are given a set A and  other sets.
# # Your job is to find whether set A is a strict superset of each of the N sets.
# # Print True, if A is a strict superset of each of the N sets. Otherwise, print False.
# # A strict superset has at least one element that does not exist in its subset.

# # Example
# # Set ([1,3,4])is a strict superset of set ([1,3]).
# # Set ([1,3,4])is not a strict superset of set ([1,3,4]).
# # Set([1,3,4]) is not a strict superset of set ([1,3,5]).

# # Input Format
# # The first line contains the space separated elements of set A.
# # The second line contains integer n, the number of other sets.
# # The next n lines contains the space separated elements of the other sets.

# # Constraints
# # 0<len(set(A)) < 501
# # 0<N<21
# # 0<len(otherSets)<101

# # Output Format
# # Print True if set A is a strict superset of all other N sets. Otherwise, print False.

# # Sample Input 0
# # 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
# # 2
# # 1 2 3 4 5
# # 100 11 12

# # Sample Output 0
# # False

# # Explanation 0
# # Set A is the strict superset of the set ([1,2,3,4,5]) but not of the set([100,11,12]) because 100 is not in set A .
# # Hence, the output is False.


# # Input reading
# A = set(input().split())
# n = int(input())

# is_strict_superset = True

# for _ in range(n):
#     other_set = set(input().split())
#     if not (A > other_set):  # Check if A is a strict superset of other_set
#         is_strict_superset = False
#         break
# print(is_strict_superset)




# # Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.
# # One fine day, a finite number of tourists come to stay at the hotel.
# # The tourists consist of:
# # → A Captain.
# # → An unknown group of families consisting of K members per group where K ≠ 1.
# # The Captain was given a separate room, and the rest were given one room per group.
# # Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear K times per group except for the Captain's room.
# # Mr. Anant needs you to help him find the Captain's room number.
# # The total number of tourists or the total number of groups of families is not known to you.
# # You only know the value of K and the room number list.

# # Input Format
# # The first line consists of an integer,K , the size of each group.
# # The second line contains the unordered elements of the room number list.

# # Constraints
# # 1<K<1000

# # Output Format
# # Output the Captain's room number.

# # Sample Input
# # 5
# # 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 

# # Sample Output
# # 8

# # Explanation
# # The list of room numbers contains 31 elements. Since K is 5, there must be 6 groups of families. In the given list, all of the numbers repeat 5 times except for room number 8.
# # Hence,8 is the Captain's room number.



# def find_captain_room(k, room_list):
#     unique_rooms = set(room_list)
#     sum_all = sum(room_list)
#     sum_unique = sum(unique_rooms)
    
#     # Calculate the captain's room number
#     captain_room = (sum_all - k * sum_unique) // (1 - k)
    
#     return captain_room

# # Read input
# k = int(input().strip())
# room_list = list(map(int, input().strip().split()))

# # Find and print the captain's room number
# captain_room_number = find_captain_room(k, room_list)
# print(captain_room_number)
