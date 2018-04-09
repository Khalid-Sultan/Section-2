def isArmstrong(n):
    c=0
    a=n
    while a>=1:
        a=a/10
        c=c+1
    b=n
    s=0
    while b>=1:
        d=b%10
        s=s+(d**c)
        b=b//10
    if s==n:
        return True
    else:
        return False
def main():
    for i in range(1,10001):
        if isArmstrong(i):
            print(i)
main()
