n=int(input("How many numbers do you want?"))
m=int(input("enter a number:"))
s=0
j=m
k=m
for i in range(0,n-1):
    m=int(input("enter a number:"))
    s=s+m
    if j<m:
        j=m
    if j>m:
        k=m
a=s/n
print("the max value of the numbers is",j)
print("the min value of the numbers is",k)
print("the sum of the numbers is",s)
print("the average of the numbers is",a)
