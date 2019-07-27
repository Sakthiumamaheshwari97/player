jy,ik,lo=list(input().split())
res=''
for letter in jy:
    for letter in ik:
       if(letter(jy)!=letter(ik)):
           res=res+letter
jim=len(res)
if(jim==lo):
    print("yes")
else:
    print("no")
