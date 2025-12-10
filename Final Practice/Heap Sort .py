import random as r

def heapSort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr,n,i)

    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr,i,0)

def heapify(arr,n,i):
    largest = i
    left = i*2 + 1
    right = i*2 + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

unsorted_arr = [r.randint(1,30) for _ in range(15) ] 

print(unsorted_arr)
heapSort(unsorted_arr)
print(unsorted_arr)
