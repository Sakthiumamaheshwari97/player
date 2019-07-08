un=int(input())
io=input()
ss=[]
for i in io:
     if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
                    continue
     else:
         ss.append(i)
print(''.join(map(str,ss)))
         
         
