def array_copy(arr):
    copied_arr = [None]*len(arr)
    for i in range(len(arr)):
        copied_arr[i] = arr[i]
    return copied_arr

a = [5,3,4,6,7,2,1,0]
b = array_copy(a)
print('Copied Array :',b)