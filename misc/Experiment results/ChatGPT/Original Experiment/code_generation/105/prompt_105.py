def by_length(arr):
    num_to_str = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    arr = sorted([x for x in arr if x in range(1, 10)])
    arr.reverse()
    return [num_to_str.get(x,x) for x in arr]
