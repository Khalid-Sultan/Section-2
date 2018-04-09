n=int(input("enter a number"))
i=10
j=1
s=0
while i<=n:
    i=10**j
    if i==10:
        k=int(n%i)
    else:
        k=int(((n%i)-(n%(i/10)))/(i/10))
    print(k,end='')
    s=s+k
    j=j+1
print()
print(s)
