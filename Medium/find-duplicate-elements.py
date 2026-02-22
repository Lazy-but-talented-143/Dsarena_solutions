def sol():
    letter=""
    s=input()
    for ch in s:
        if s.count(ch)>1:
            letter=letter+ch
            s=s.replace(ch,"")
        if letter=="":
            return None
    return letter
print(sol())