n,k=map(int,input().split())
h=list(map(int,input().split()))
for i in range(0,k):
    h=[h[-1]]+h[:-1]
print(*h,end=' ')
    
