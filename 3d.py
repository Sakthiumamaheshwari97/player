num,sum=map(int,input().split())
waste=input()
arr=list(map(int,input().split()))
arr1=list(map(int,input().split()))
list=[]
for i in range(len(arr1)):
    arr.append(arr1[i])
    list.append(str(max(arr)))
print(" ".join(list))
