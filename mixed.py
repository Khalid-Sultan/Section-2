for j in range(1,10,2):
    for l in range (j):
        print(j,end=' ')
    for i in range(j,10):
        print('*',end=' ')
    for k in range (j+1,10):
        print('', end=' ')
    print()
for j in range(1,10):
    for k in range (j+1,10):
        print(j, end=' ')
    for i in range(j):
        print('*',end=' ')
    print()
