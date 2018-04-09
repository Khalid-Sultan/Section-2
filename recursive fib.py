n=int(input("Enter the number of fib. numbers: "))
def fib(n):
    c=0
    a=1
    b=1
    while c<n:
        print(a)
        a,b=b,a+b
        c=c+1
fib(n)
