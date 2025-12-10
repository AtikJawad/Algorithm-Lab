def QuickSort(arr):
    if len(arr)<=1:
        return arr

    pivot = arr[-1] # taking last element of the arr as pivot
    left_arr = [x for x in arr[:-1] if x < pivot]
    right_arr = [x for x in arr[:-1] if x >= pivot]

    return QuickSort(left_arr)+ [pivot] + QuickSort(right_arr)

unsorted_list = list(map(int, (input("Enter numbers sperated by space: ").strip()).split()))

sorted = QuickSort(unsorted_list)

for number in sorted:
    print(number, end=" ")
