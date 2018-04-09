s=0
i=9
for i in range(9,22,1):
    s=s+i
    if i<21:
        print(i,'+ ',end='')
    else:
        print(i,end='')
print(' =',s)
