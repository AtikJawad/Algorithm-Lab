'''
- Use any sorting algorithm to sort between 500 to 1000 numbers.  
- The numbers should be randomly generated, each ranging from greater than 100 to less than 1000.  
- Use a random function to generate these numbers.  
- Print the sorted output to a file (not on the terminal) 
'''

import random as r

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle= len(arr)//2 # Equivalent to int(len(arr)/2) but faster

    left_arr = merge_sort(arr[:middle])
    right_arr = merge_sort(arr[middle:])

    return merge(left_arr,right_arr)

def merge(left,right):
    output=[]
    i=j=0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            output.append(left[i])
            i+=1
        else:
            output.append(right[j])
            j += 1
    # Adding the remaining element
    for x in range(i, len(left)):  #output.extend(left[i:])
            output.append(left[x])

    for y in range(j, len(right)):  #output.extend(right[j:])
            output.append(right[y])

    return output


num_elements=r.randint(500, 1000)

unsorted_list=[]
for i in range(num_elements):
    unsorted_list.append(r.randint(101, 999)) # as per condition

sorted_list = merge_sort(unsorted_list)

#Saving the sorted list onto a File
file_name="C:/Users/hands/Desktop/output.txt"


with open(file=file_name, mode="w") as file:
    for number in sorted_list:
        file.write(f"{number}\n")

print("The file is created!!")
print(f"Total {num_elements} numbers are sorted in the file")
