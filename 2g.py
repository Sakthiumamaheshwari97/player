lub,dub=map(int,input().split())
for i in range(lub,10000):
   if(i%lub==0 and i%dub==0):
      print(i)
      break
