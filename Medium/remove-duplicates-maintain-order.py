def sol():
    letter=""
    s=input()
    for ch in s:
        if s.count(ch)==1:
            letter=letter+ch
        elif s.count(ch)>1:
            letter=letter+ch.replace(" ","")
            s=s.replace(ch,"")
    print(letter.replace(""," "))
sol()