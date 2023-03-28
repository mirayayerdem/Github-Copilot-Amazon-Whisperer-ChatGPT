def exchange(lst1, lst2):
    even_nums = [x for x in lst2 if x % 2 == 0]
    odd_nums = [x for x in lst1 if x % 2 != 0]
    if len(even_nums) >= len(odd_nums):
        return "YES"
    else:
        return "NO"
