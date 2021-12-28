def fibo(n):
    #check if input it 0
    # print incorrect input
    if n<0:
        print("Incorrect Input")
    ## if n is equal to 0
    ## print o
    elif n == 0:
        return 0
    # check if n == 1 or n == 2
    # return 1
    elif n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1)+(n-2)
        print(n)



print(fibo(9))