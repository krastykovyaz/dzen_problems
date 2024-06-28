# quick sort

def qsrt(arr):
    if len(arr) <= 1:
        return arr
    mid = arr[len(arr) // 2]
    left = [item for item in arr if item < mid]
    right = [item for item in arr if item > mid]
    mode = [item for item in arr if item == mid]
    return qsrt(left) + mode + qsrt(right)

if __name__=='__main__':
    arr = [2,5,6,4,3,2,8]
    print(qsrt(arr))
