def fib(n):
    if n<1:
        return 1
    else:
        return (fib(n-1) + fib(n-2))

def main():
    n=int(input("How many fibonacci terms do you want to generate?"))
    for i in range(n):
        print(fib(i))
main()
