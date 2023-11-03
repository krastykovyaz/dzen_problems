# delete zeros from array

def zero_remover(arr):
    if len(arr) < 1:
        return []
    if len(arr) == 1 and arr[0] != 0:
        return arr
    i = 0
    j = 0
    while i < len(arr) and j < len(arr):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
        i += 1
    while i > 0 and arr[i - 1] == 0:
        arr.pop()
        i -= 1


if __name__ == '__main__':
    orig_arr = [0, 0, 0, 0, 0, 1000, 0, 0]
    zero_remover(orig_arr)
    assert orig_arr == [1000]
