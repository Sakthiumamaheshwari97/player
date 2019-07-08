n,k=map(int,input().split())
h=list(map(int,input().split()))
p=[]
for i in h[-1:]:
    if(k>0):
        p.append(i)
        h=-1
print(p)
   
    
