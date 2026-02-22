from typing import List

def linearSearch(arr: List[int], target: int) -> int:
    # Your code here
    for ch in arr:
        if ch==target:
            return arr.index(ch)
    return -1
    pass
# Read input
arr = list(map(int, input().split()))
target = int(input())
print(linearSearch(arr, target))