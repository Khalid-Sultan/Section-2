n=int(input("Enter the size of the list:"))
b=list()#or b=[]
s=0

#Accept n numbers into a list

for a in range(n):
    c=eval(input("Enter a number in list: "))
    b.append(c)
print(b)
print()

#Sum of Elements in a list

for d in range(n):
    s=s+b[d]
print("The sum of the numbers is",s)
print()

#Smallest number in a list

def mlist(a):
    m=b[0]
    for i in range(n):
        if b[i]<m:
            m=b[i]
    return m
print("The minimum of the numbers is",mlist(a))
print()

#Sinosoidality

def isSonusoid():
    c=0
    for d in range(n):
        if d!=n-1:
            if e[d]%2==0 and e[d+1]%2==0:
                c=c+1
            elif e[d]%2!=0 and e[d+1]%2!=0:
                c=c+1
            else:
                c=c
    if c==0:
        return True
    else:
        return False

def main():
    n=int(input("Enter the size of the list:"))
    e=list()#or e=[]
    for a in range(n):
        x=eval(input("Enter a number in list: "))
        e.append(x)
    print(e,"is sinusoidally", isSonusoid())
main()
