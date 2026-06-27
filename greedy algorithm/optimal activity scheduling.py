'''Conference Hall Manager: Optimal Activity Scheduling

You are the event coordinator of a large conference center. Multiple activities are scheduled throughout the day, and each activity has a start time and an end time. However, the venue has only one hall, so no two activities can overlap.

Your goal is to select the maximum number of non-overlapping activities that can be scheduled in the hall.

You are given the start and end times of n activities. Write a program to choose the maximum number of activities that can be performed by a single person or in one room, assuming a person/room can only work on a non-overlapping schedule.



Input Format

The first line contains an integer n, the number of activities.
The next n lines each contain two space-separated integers: start and end times of the activity.


Output Format

A single integer representing the maximum number of non-overlapping activities that can be scheduled.


Example 1

Sample Input 1

6

1 3

3 4

0 5

5 7

8 9

5 9



Sample Output 1

4



Explanation

Optimal selection of activities:
(1, 3)
(3, 4)
(5, 7)
(8, 9)
These activities do not overlap and maximize the count.


Example 2

Sample Input 2

3

10 20

20 30

15 25



Sample Output 2

2



Explanation

Optimal selection:
(10, 20)
(20, 30)
(15, 25) overlaps with both, so it’s excluded.
'''

# def endTime(activity):
#   return activity[1]
  
def findConference(activity):
  
  activity.sort(key = lambda x : x[1])
  count = 0
  l_end = 0

  for s,e in activity:
    if l_end  <= s:
      count += 1
      l_end = e

  return count
  
if __name__ == '__main__' :
  n = int(input())
  activity = []
  
  for i in range(n):
    s,e = map(int, input().split())
    activity.append((s,e))
    
  print(findConference(activity))