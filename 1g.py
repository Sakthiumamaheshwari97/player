kt=list(input())
for i in range(0,len(kt),2):
  kt[i],kt[i+1]=kt[i+1],kt[i]
print(''.join(kt))
