def search(data,target,low,high):
    print(data)
    if low > high:
        return False
    else:
        mid = (low+high)//2    
        print("middle value",mid)

        if target == data[mid]:
            return True
        elif target < data[mid]:
            return search(data,target,low,mid-1)
        else:
            return search(data,target,mid+1,high)


data = [12,34,45,231,67,1,8,9,10,54,87]
target = 10
print(search(data,target,0,len(data)-1))    