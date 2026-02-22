def isRotation():
    #print(s,m)
    if len(s)==len(m):
        letter=""
        for k in range(0,len(m)):
            n1=m[k:]+m[:k]
            letter=letter+n1
        if s in letter:
            return True
    return False
# Read input
s = input()
m = input()
print(isRotation())