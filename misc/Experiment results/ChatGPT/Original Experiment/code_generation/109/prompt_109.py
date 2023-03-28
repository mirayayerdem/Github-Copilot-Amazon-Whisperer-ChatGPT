def move_one_ball(arr):
    if len(arr) == 0:
        return True
    for i in range(len(arr)):
        if arr == sorted(arr[i:] + arr[:i]):
            return True
    return False
