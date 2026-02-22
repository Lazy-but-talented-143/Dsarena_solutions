def countVowelsConsonants(s: str) -> str:
    # Your code here
    c=0
    v=0
    vowels="aeiou"
    consonants="bcdfghjklmnpqrstvwxyz"
    for ch in s:
        if ch in vowels:
            v=v+1
        elif ch in consonants:
            c=c+1
    print(f"{v} {c}")
    pass
# Read input
s = input().lower()
countVowelsConsonants(s)