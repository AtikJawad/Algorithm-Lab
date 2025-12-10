import random as r

def MergeSort(arr):
    if len(arr)<=1:
        return arr
    middle= len(arr)//2

    left_arr = MergeSort(arr[:middle])
    right_arr = MergeSort(arr[middle:])

    return Merge(left_arr,right_arr)

def Merge(Left,Right):
    merged = []
    i=j=0

    while i < len(Left) and j < len(Right):
        if Left[i] < Right[j]:
            merged.append(Left[i])
            i+=1
        else:
            merged.append(Right[j])
            j+=1

    for x in Left[i:] :
        merged.append(x)
    for y in Right[j:] :
        merged.append(y)

    return merged

totalnumber = r.randint(500,600)

unsorted= []
for i in range (totalnumber):
    number = r.randint(100,1000)
    if number not in unsorted:
        unsorted.append(number)

sorted = MergeSort(unsorted)

filename = "G:\\Algo lab\\input files\\Merge Sort output.txt"

with open (filename, "w") as f:
    f.write("UNSORTED: ")
    for number in unsorted:
        f.write(f"{number} ")
    f.write("...........................")
    f.write("\n\n")
    f.write("SORTED: ")

    for number in sorted:
        f.write(f"{number} ")

print("The file is created!!")
print(f"Total {totalnumber} numbers are sorted in the file")
