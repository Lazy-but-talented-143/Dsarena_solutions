from typing import List
def sol():
    # Your code here
    if len(strs)==3:
        letter=""
        ch0=strs[0]
        ch1=strs[1]
        ch2=strs[2]
        m=min(len(ch0),len(ch1),len(ch2))
        for i in range(0,m):
            if ch0[i]==ch1[i]==ch2[i]:
                letter=letter+ch0[i]
        print(letter)
    elif len(strs)==2:
        letter=""
        ch0=strs[0]
        ch1=strs[1]
        m=min(len(ch0),len(ch1))
        for i in range(0,m):
            if ch0[i]==ch1[i]:
                letter=letter+ch0[1]
        print(letter)
    pass
# Read input
strs = input().split(',')
sol()