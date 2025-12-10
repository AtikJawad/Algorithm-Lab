def StringSearch(T,P):
    m = len(P)
    n = len(T)

    for i in range(n - m + 1):
        j=0
        while j<m and T[i+j] == P[j]:
            j += 1
        if j==m:
            print(f"Pattern found at index {i}")

text = input("Enter Text: ")
pattern = input("Enter Pattern: ")

StringSearch(text,pattern)

