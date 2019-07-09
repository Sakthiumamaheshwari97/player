aks=input()
ball='0ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
call=''
for i in aks:
  if i in ball:
    t=ball.index(i)
    t=t+3
    call=call+ball[t]
print(call)
