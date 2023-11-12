# Minimum house number
PrepBuddy lives in a colony, where N houses are built in a single row numbered from 
0 to N 1. The first house has a house number 0, the second house has a house number 1 and so on, every house pays some rent at the end of the month.
Help PrepBuddy in finding out the house number of the house paying the minimum rent.
Note: All house rents are unique.




n = int(input())
i=0
j=0
for i in range(0,n):
  len = int(input())
  arr = list(map(int,input().split()))
  min = 100000001
  for j in range(0,len):
    if(arr[j]<=min):
      min=arr[j]
      pos = j
  print(pos)