n=int(input("enter a number to check for palidrome, or zero to terminate"))
def reverse(n):
    rev=0
    while n>0:
        rev=rev*10+n%10
        n=n//10
    return rev
print('reverse of',n,'is',reverse(n))
def ispalindrome(n):
    return (n==reverse(n))
def main():
    while True:
        if n==0:
            break
        elif ispalindrome(n):
            print(n,'is a palindrome number.')
        else:
            print(n,'is not a palindrome number.')
        return n
main()
