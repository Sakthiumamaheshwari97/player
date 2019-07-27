jim,jam=list(map(int,input().split()))
k=[]
for i in range(jim,jam+1):
    j=1
    while j*j<=i:
       if j*j==i:
           k.append(i)
       j=j+1
    i=i+1
print(len(k))
