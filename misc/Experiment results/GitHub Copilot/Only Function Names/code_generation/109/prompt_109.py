
def move_one_ball(arr):
    """ (list of int) -> NoneType
    Move the first ball in arr to the end of the list.
    """
    arr.append(arr.pop(0))