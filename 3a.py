at,bt=list(map(int,input().split()))
ct,dt=list(map(int,input().split()))
et,ft=list(map(int,input().split()))
if at==bt or ct==dt or et==ft or at==ct==ft or bt==dt==et:
    print('yes')
else:
    print('no')
