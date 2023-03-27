
def solve(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    else:
        return solve(N-1) + solve(N-2)
