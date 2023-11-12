n = int(input())
for i in range(0,n):
  len = 0
  flag=0
  len =int(input())
  arr=list(map(int,input().split()))
  for j in range(0,len):
    if(arr[j]==1):
      flag = flag + 1
      pos = j
  if(flag==0):
    print(-1)
  else:
    print(pos)