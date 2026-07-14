import math
def is_fionacci(n):
    return(math.isqrt(5*n*n+4)**2 == 5*n*n+4)
num = int(input("Enter a number :"))
if is_fionacci(num):
    print(num,"is a fibonacci number")
else:
    print(num,"is not a fibonacci number")