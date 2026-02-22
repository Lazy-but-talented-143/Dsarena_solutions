def factorialIterative(n: int) -> int:
    # Your iterative solution here
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
    pass
def factorialRecursive(n: int) -> int:
    # Your recursive solution here
    if n==0:
        return 1
    else:
        return n*factorialRecursive(n-1)
    #    return n
    pass
# Read input
n = int(input())
print(f"{factorialIterative(n)} {factorialRecursive(n)}")