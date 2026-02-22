from typing import List

def selectionSort(arr: List[int]) -> List[int]:
    # Your code here
    i=0
    for ch in arr:
        a=arr[i:]
        i=i+1
        if ch>min(a):
            m1=arr.index(min(a))
            m2=arr.index(ch)
            arr[m1],arr[m2]=arr[m2],arr[m1]
    return arr
    pass
# Read input
arr = list(map(int, input().split()))
result = selectionSort(arr)
print(' '.join(map(str, result)))