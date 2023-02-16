
def bin_se(arr, a,b, x):
 
    if b >= a:
        mid = (b + a) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return bin_se(arr, a, mid - 1, x)
        else:
            return bin_se(arr, mid + 1,b, x)
    else:
        return -1
arr = [6,8,3,8,3,22,85,25,48,5,13,68,3,67,47,24,74,45 ]
x = 22
result = bin_se(arr, 0, len(arr)-1, x)
if result != -1:
    print("Element is present at ", str(result))
else:
    print("Element is not present ")