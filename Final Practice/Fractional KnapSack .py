def frac_Knapsack(values, weight, capacity):

    n= len(values)
    ratio = [(values[i]/weight[i]) for i in range(n)]

    Maximum_profit = 0

    items=[(i+1) for i in range(n)]

    print("Item\t Value\t weight\t Remaining Capacity")
    while capacity > 0:
        max_ratio = max(ratio)

        max_ratio_idx = ratio.index(max_ratio) # index of the max ratio

        v = values[max_ratio_idx]
        w = weight[max_ratio_idx]
        

        if w < capacity:
            Maximum_profit += v
            capacity -= w
            ratio[max_ratio_idx] = -1 # -1 will  represent the item is taken
        
        else:
            Maximum_profit += max_ratio * capacity
            capacity = 0 # ensuring the while loop terminates...

        print(f"{items[max_ratio_idx]}\t {v}\t {w}\t {capacity}")   

    return  Maximum_profit


Item = int(input("Total Items: "))
W = int(input("Enter KnapSack Capacity: "))

print(f"Enter Values of {Item} items: ")
values = [int(input())  for i in range(Item)]
print(f"Enter weights of {Item} items: ")
weights = [int(input())  for i in range(Item)]

Total_profit = frac_Knapsack(values, weights, W)
print("________________________________________________")
print(f"Maximum Possible Profit : {Total_profit}")



        
