from typing import List

def missingNumber(nums: List[int]) -> int:
    # Your code here
    num1=set(nums)
    num1=list(num1)
    num1.sort()
    for i in range(0,max(num1)+1):
        if i not in num1:
            return i
    return i+1
        #print(i+1)
    #print(num1)
    pass
# Read input
nums = list(map(int, input().split()))
print(missingNumber(nums))