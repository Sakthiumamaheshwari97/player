aks=input()
ball='0ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
call=''
for i in aks:
  if i in ball:
    t=ball.index(i)
    t=t+3
    call=c+ball[t]
print(call)
