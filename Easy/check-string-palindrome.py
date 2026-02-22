def isPalindrome(s: str) -> bool:
    # Your code here
    s1=s[::-1]
    if s1==s:
        return True
    return False
    pass

# Read input
s = input().lower().replace(" ","")
print(isPalindrome(s))