len = int(input())
arr = list(map(int,input().split()))
odd = []
even = []
for i in range(0,len):
  if(arr[i]%2==0):
    print(arr[i],end=' ')
print()
for j in range(0,len):
  if(arr[j]%2!=0):
    print(arr[j],end=' ')
