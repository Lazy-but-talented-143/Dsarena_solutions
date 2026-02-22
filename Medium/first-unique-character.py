def firstUniqChar(s: str) -> int:
    # Your code here
    for ch in s:
        if s.count(ch)==1:
            return s.index(ch)
    return -1
    pass
# Read input
s = input()
print(firstUniqChar(s))