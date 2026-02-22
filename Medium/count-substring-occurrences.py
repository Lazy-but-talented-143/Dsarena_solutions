def countSubstring(s: str, sub: str) -> int:
    # Your code here
    n1=len(s)
    n2=len(sub)
    count=0
    for i in range(n1-n2+1):
        if s[i:i+n2]==sub:
            count=count+1
    return count
    pass
# Read input
s = input()
sub = input()
print(countSubstring(s, sub))