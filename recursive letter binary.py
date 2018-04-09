def main():
    for value in range(A,Z):
        print("The binary value is",decimalToBinary(value))

def decimalToBinary(value):
    result=""
    b=ord(value)
    a=int(b)
    while a!=0:
        bit=a%2
        result=str(bit)+result
        a=a//2
    return result
main()
