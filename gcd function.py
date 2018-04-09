n=int(input("enter the first number:"))
m=int(input("enter the second number:"))
def gcd(n,m):
    i=1
    while i<= n and i<=m:
        if n%i==0 and m%i==0:
            d=i
        i=i+1
    return d
print("their gcd is", gcd(n,m))
