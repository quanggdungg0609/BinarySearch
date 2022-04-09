def naive_search(l, target):
    for i in range (len(l)):
        if i==target:
            return i
    return -1

#oonly use in sorted list
def binary_search(l,target, low=None,high=None):
    if low is None:
        low=0
    if high is None:
        high=len(l)-1
    if high < low:
        return -1
    mid_point=(low+high)//2
    if l[mid_point]==target:
        return mid_point
    elif target<l[mid_point]:
        return binary_search(l,target,low,mid_point-1)
    else:
        return binary_search(l,target,mid_point+1,high)

l=[1,3,5,10,15,20]
print(binary_search(l,3))