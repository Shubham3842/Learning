def insertion_sort(A):
    for k in range(1,len(A)):
        curr = A[k]
        j = k
        while j > 0 and A[j-1] > curr:
            A[j] = A[j-1]
            j-=1 
        A[j] = curr
        print(A)       

A = [10,2,15,6,57,1,2]
print('Before sorting',A)
insertion_sort(A)
print('After sorting',A)       
