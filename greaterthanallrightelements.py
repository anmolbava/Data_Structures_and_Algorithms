n = int(input())
arr = list(map(int,input().split()))
j = 0
 for j in range(len-1,0,-1):
   if(j==len-1):
    print(arr[j],end="")
   else: 
    flag = 0
    k = j+1
    while(k<=len-1):
     if(arr[k]>=arr[j]):
      flag = flag + 1
      k=k+1
    if(flag==k):
      print(arr[j],end="")



2nd approach
times = int(input())
i=0
len =0
for i in range(0,times):
 len = int(input())
 arr = list(map(int,input().split()))
 j = 0
 for j in range(0, len): 
  for k in range(j+1,len): 
    if(arr[j]<=arr[k]): 
     break
  if k == len-1: # If loop didn't break 
    print(arr[j])