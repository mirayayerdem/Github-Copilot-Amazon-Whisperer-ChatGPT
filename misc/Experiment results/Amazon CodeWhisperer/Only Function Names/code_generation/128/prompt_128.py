
def prod_signs(arr):
    if arr[0] < 0:
        if arr[1] < 0:
            return -1
        else:
            return 1
    else:
        if arr[1] < 0:
            return 1
        else:
            return 0

