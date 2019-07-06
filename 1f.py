gut,hut=input().split()
if(len(gut)==len(hut)):
      for i in gut:
          u=gut.count(i)
      for i in hut:
          v=hut.count(i)
      if(u==v):
        print("yes")
      else:
        print("no")
else:
   print("no")
