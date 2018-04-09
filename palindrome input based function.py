w=input("enter a number or word")
def is_palindrome(w):
    if len(w) < 2:
        print("ERROR: input contains less than 2 characters.")
    else:
        i=0
        j=len(w)
        s=0
        for i in range(i,len(w),1):
            k=w[i]
            l=w[j-1]
            if k==l:
                s=s
            else:
                s=s+1
            j=j-1
        if s==0:
            print(w,'is a palindrome')
        else:
            print(w,'is not a palindrome')
is_palindrome(w)
