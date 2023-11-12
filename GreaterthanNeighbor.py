




n = int(input())
for i in range(0,n):
  len = 0
  len = int(input())
  arr = list(map(int,input().split()))
  flag = 0
  for j in range(0,len):
    if(j==0):
      if(arr[j]>arr[j+1]):
        pos = j
        print(pos,end=' ')
        flag +=1
    elif(j==(len-1)):
      if(arr[j]>arr[j-1]):
        pos = j
        print(pos,end=' ')
        flag +=1
    else:
      if(arr[j]>arr[j-1] and arr[j]>arr[j+1]):
        pos = j
        print(pos,end=' ')
        flag +=1
  if(flag == 0):
    print("-1")
  print()