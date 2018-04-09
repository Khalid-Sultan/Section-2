def main():
    for value in range (10,48):
        print("The binary value of",value,"base 10 =",decimalToBinary(value),"base 2")

def decimalToBinary(value):
    result=""
    while value!=0:
        bit=value%2
        result=str(bit)+result
        value=value//2
    return result
main()
