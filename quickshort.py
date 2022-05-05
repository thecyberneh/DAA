def partition(arr,start,end):

    pivote=arr[start]
    low=start+1
    high=end

    while True:

        while low <= high and arr[high] >= pivote:
            high=high-1

        while low <= high and arr[low] <= pivote:
            low=low+1


        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break

    arr[start], arr[high] = arr[high], arr[start]

    return high

def quickshort(arr,start,end):
    if start >= end:
        return

    p=partition(arr,start,end)
    quickshort(arr,start,p-1)
    quickshort(arr,p+1,end)

arr = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]

quickshort(arr, 0, len(arr) - 1)
print(arr)