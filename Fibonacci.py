# fibonacci series has number in which each number is sum of two preceeding numbers
# 0 1 1 2 3 5 8 13 21...n
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
n = int(input("number of elements"))
print(a,b,end=" ")
while n-2: #
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    n=n-1


def fibonacci(number1,number2,end=" "):
    while n-2:
        number3 =number1+number2
        number1 = number2
        number2 = number3
        print(number3,end=" ")
        n=n-1