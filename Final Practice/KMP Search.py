def kmpSearch(text,pattern):
    if pattern == "":
        return 0
    lps = build_lps(pattern)

    t = 0
    p = 0

    while t< len(text):
        if text[t] == pattern[p]:
            t+=1
            p+=1

            if p == len(pattern):
                return t - p
        else:
            if p > 0:
                p = lps[p-1]
            else:
                t+=1
    return -1

def build_lps(pattern):
    lps= [0]*len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length+=1
            lps[i] = length
            i+=1

        else:
            if length > 0:
                length = lps[length -1]
            else:
                lps[i] = 0
                i+=1
    return lps

text = input("Text: ")
pattern = input("Pattern: ")

pos = kmpSearch(text, pattern)

if pos != -1:
    print(f"Pattern found at index {pos}")
else:
    print("Pattern not found")
