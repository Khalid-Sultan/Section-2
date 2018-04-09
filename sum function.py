s=0
def sum_range(start,stop,step):
    sum=0
    for i in range(start,stop,step):
        sum+=i
    return sum

print('9 + 10 + ... + 21 =',sum_range(9,22,1)s)
print('first summation done')
print('37 + 38 + ... + 50 =',sum_range(37,51,1))
print('second summation done')
print('45 + 46 + ... + 66 =',sum_range(45,67,1))
print('third summation done')
print('4 + 11 + ... + 60 =',sum_range(4,61,7))
print('fourth summation done')
