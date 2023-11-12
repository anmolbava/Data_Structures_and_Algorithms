times = 1
length=0

for i in range(0,times):
  length = int(input())
  arr=list(map(int,input().split()))
  mult=1
  for j in range(0,length-1):
    mult=mult * arr[j]
  print(mult)


  or submitted code successfullly below
n = int(input())
len = 0
j = 0 
i = 0
for j in range(0,n):
  len = int(input())
  arr=list(map(int,input().split()))
  mult = 1
  for i in range(0,len):
    mult = mult * arr[i]
  print(mult)