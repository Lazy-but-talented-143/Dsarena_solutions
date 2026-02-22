from typing import List

def sol():
    n=[]
    for i in range(0,len(nums)):
        for j in range(len(nums)):
            if i!=j:
                if nums[i]+nums[j]==target:
                    n.append(i)
                    n.append(j)
                    if len(n)>3:
                        print(f"{n[0]} {n[1]}")     
    pass
# Read input
nums = list(map(int, input().split()))
target = int(input())
#result = twoSum(nums, target)
#print(result[0], result[1])
sol()