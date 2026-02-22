def reverseNumber(n: int) -> int:
    n1=str(abs(n))
    n2=n1[::-1]
    n3=abs(int(n2))
    if n<0:
        print(f"-{n3}")
    else:
        print(n3)
    pass
# Read input
n = int(input())
reverseNumber(n)