ip,rs=map(int,input().split())
s=[]
for i in range(ip+1,rs+1):
    for x in range(2,i):
       if(i%x==0): 
           break
    else:
         s.append(x)
print(len(s)+1)
