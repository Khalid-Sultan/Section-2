import random
n=random.randint(0,101)
for i in range(0,7):
    j=int(input("enter a number:"))
    if j==n:
        print("correct, you have found the number!")
        break
    elif j>n:
        print("your guess is more than the number.")
    else:
        print("your guess is less than the number.")
if j!=n:
    print("you lost! The number was",n)
