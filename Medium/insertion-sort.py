from typing import List

def selectionSort(arr: List[int]) -> List[int]:
    # Your code here
    limit=0
    j=0
    while limit<=3:
        limit=limit+1
        for ch in arr:
            for i in range(0,len(arr)-1):
                j=i+1
                if ch>=0:
                    if arr[i]<ch<arr[j] and arr[i]<ch or ch<arr[j]:
                        arr.remove(ch)
                        arr.insert(i,ch)
                        break;
                elif ch<0:
                    if arr[i]>ch>arr[j] or arr[i]>ch:
                        arr.remove(ch)
                        arr.insert(i,ch)
                        break;
    return arr
    pass
# Read input
arr = list(map(int, input().split()))
result = selectionSort(arr)
print(' '.join(map(str, result)))