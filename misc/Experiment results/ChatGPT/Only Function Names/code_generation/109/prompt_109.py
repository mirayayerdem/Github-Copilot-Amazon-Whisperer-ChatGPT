
def move_one_ball(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                if i == 0:
                    if j == 0:
                        if arr[i+1][j] == 0 and arr[i][j+1] == 0:
                            arr[i][j] = 0
                            return (i+1, j)
                    elif j == len(arr[i])-1:
                        if arr[i+1][j] == 0 and arr[i][j-1] == 0:
                            arr[i][j] = 0
                            return (i+1, j)
                    else:
                        if arr[i+1][j] == 0 and arr[i][j-1] == 0 and arr[i][j+1] == 0:
                            arr[i][j] = 0
                            return (i+1, j)
                elif i == len(arr)-1:
                    if j == 0:
                        if arr[i-1][j] == 0 and arr[i][j+1] == 0:
                            arr[i][j] = 0
                            return (i-1, j)
                    elif j == len(arr[i])-1:
                        if arr[i-1][j] == 0 and arr[i][j-1] == 0:
                            arr[i][j] = 0
                            return (i-1, j)
                    else:
                        if arr[i-1][j] == 0 and arr[i][j-1] == 0 and arr[i][j+1] == 0:
                            arr[i][j] = 0
                            return (i-1, j)
                else:
                    if j == 0:
                        if arr[i-1][j] == 0 and arr[i+1][j] == 0 and arr[i][j+1] == 0:
                            arr[i][j] = 0
                            return (i, j+1)
                    elif j == len(arr[i])-1:
                        if arr[i-1][j] == 0 and arr[i+1][j] == 0 and arr[i][j-1] == 0:
                            arr[i][j] = 0
                            return (i, j-1)
                    else:
                        if arr[i-1][j] == 0 and arr[i+1][j] == 0 and arr[i][j-1] == 0 and arr[i][j+1] == 0:
                            arr[i][j] = 0
                            return (i, j)
