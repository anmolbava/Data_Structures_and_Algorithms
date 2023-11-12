times = int(input())
for i in range(0,times):
  len = int(input())
  expected = 0
  arr = list(map(int,input().split()))
  expected = arr[0]
  for j in range(0,len-1):
    if(arr[j] == expected):
      expected = arr[j] + 1
    else:
      print(expected)