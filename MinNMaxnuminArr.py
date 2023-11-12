
t = int(input())
for i in range(0,t):
  n = int(input())
  arr = [int(ele) for ele in input().split()]
  min = 1000001
  max = -1000001
  for j in range(0,n):
    if(arr[j]<min):
      min = arr[j]
    if(arr[j]>max):
      max = arr[j]
  print(min,max)
  print()