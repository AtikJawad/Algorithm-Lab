import random
def counting_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for number in arr:
        count[number] += 1

    for i in range(1,len(count)):
        count[i] += count[ i- 1]

    n= len(arr)
    sorted = [0] * n

    for i in range(n-1, -1, -1):
        num = arr[i]
        sorted[count[num] - 1] = num
        count[num] -= 1

    return sorted

arr = [random.randint(1,20) for i in range(10)]

sorted_arr = counting_sort(arr)
print(arr)
print(sorted_arr)


