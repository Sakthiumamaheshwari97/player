sa,ta=map(int,input().split())
for j in range(1,min(s,t)+1):
    if((sa%j==0) and (ta%j==0)):
        y=j
print(y)
