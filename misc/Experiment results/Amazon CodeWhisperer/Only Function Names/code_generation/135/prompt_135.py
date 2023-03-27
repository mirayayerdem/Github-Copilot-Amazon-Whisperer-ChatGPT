
def can_arrange(arr):
    arr.sort()
    for i in range(len(arr)):
        if arr[i] > i + 1:
            return False
    return True

