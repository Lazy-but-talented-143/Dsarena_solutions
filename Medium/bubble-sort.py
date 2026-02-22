from typing import List

def bubbleSort(arr: List[int]) -> List[int]:
    # Your code here
    m=len(arr)//2
    limit=0
    while limit<=m+3:
        limit=limit+1
        for i in range(0,len(arr)-1):
            #a=arr[i]
            #b=arr[i+1]
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
            #arr[i]=a
            #arr[i+1]=b
    for ch in arr:
        print(ch,end=" ")
    pass
# Read input
arr = list(map(int, input().split()))
result = bubbleSort(arr)
#print(' '.join(map(str, result)))