def match_parens(lst):
    open_count = 0
    close_count = 0
    
    for s in lst:
        for c in s:
            if c == '(':
                open_count += 1
            elif c == ')':
                if open_count > 0:
                    open_count -= 1
                else:
                    close_count += 1
    
    if open_count == 0 and close_count == 0:
        return 'Yes'
    else:
        return 'No'
