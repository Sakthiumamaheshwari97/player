fi=int(input())
gu=list(map(int,input().split()))
count=0
for i in range(0,fi+1):
        if(gu.count(i)==1):
           print(i)
        
