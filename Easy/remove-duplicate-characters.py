def removeDuplicates(s: str) -> str:
    # Your code here
    s1=s
    letter=""
    for ch in s1:
        if s1.count(ch)==1:
            letter=letter+ch
        elif s1.count(ch)>1:
            letter=letter+ch
            s1=s1.replace(ch,"")
    print(letter)
    
# Read input
s = input()
removeDuplicates(s)