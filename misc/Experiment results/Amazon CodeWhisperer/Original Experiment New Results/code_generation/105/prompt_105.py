
def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    
      If the array is empty, return an empty array:
      arr = []
      return []
    
      If the array has any strange number ignore it:
      arr = [1, -1 , 55] 
            -> sort arr -> [-1, 1, 55]
            -> reverse arr -> [55, 1, -1]
      return = ['One']
    """
    # Your code here
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return [str(arr[0])]
    else:
        arr.sort()
        arr.reverse()
        result = []
        for i in arr:
            if i < 10 and i > 0:
                if i == 1:
                    result.append("One")
                elif i == 2:
                    result.append("Two")
                elif i == 3:
                    result.append("Three")
                elif i == 4:
                    result.append("Four")
                elif i == 5:
                    result.append("Five")
                elif i == 6:
                    result.append("Six")
                elif i == 7:
                    result.append("Seven")
                elif i == 8:
                    result.append("Eight")
                elif i == 9:
                    result.append("Nine")

        return result
        