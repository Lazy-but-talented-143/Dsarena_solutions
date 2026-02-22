from typing import List

def maxSubArray(nums: List[int]) -> int:
    # Your code here - use Kadane's algorithm
    k=[0]
    for i in range(0,len(nums)):
        for j in range(len(nums)+1):
            s1=nums[i:j]
        m=0
        for i in range(0,len(s1)):
            m=m+s1[i]
            k.append(m)
    if max(k)==0:
        print(-1)
    else:
        print(max(k))
    pass
# Read input
nums = list(map(int, input().split()))
maxSubArray(nums)