def delete_duplicates():
    A = [30, 7, 7, 8, 10, 12, 12, 12]
    j = 0
    for i in range(0, len(A) - 1):
        if A[j] != A[i]:
            j += 1
            A[j] = A[i]
    for a in range(0, j+1):
        print A[a]
    
delete_duplicates()
