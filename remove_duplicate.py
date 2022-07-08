def remove_duplicate(arr):
    uniq = []
    for i in arr:
        if i not in uniq:
            uniq.append(i)
        else:
            pass
    return uniq        

a = [10,12,3,4,5,12,8,3,4,7,8,6,5,1,2]
b = remove_duplicate(a)
print("uniq element :",b)
