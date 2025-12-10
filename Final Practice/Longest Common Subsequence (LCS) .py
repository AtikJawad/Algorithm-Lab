def LCS(X,Y):
    m = len(X)
    n = len (Y)

    c = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j],c[i][j-1])
    
    lcs_str= []
    i,j = m,n 
    while i>0 and j>0:
        if X[i-1] == Y[j-1]:
            lcs_str.append(X[i-1])
            i -= 1
            j -= 1
        elif c[i-1][j] > c[i][j-1]:
            i -= 1
        else:
            j-= 1
    
    return c[m][n], ''.join(reversed(lcs_str))


s1 = input("string-1 : ")
s2 = input("string-2 :")

LCS_length, LCS_string = LCS(s1,s2)

print(f"LCS String = {LCS_string}")
print(f"LCS Length = {LCS_length}")
