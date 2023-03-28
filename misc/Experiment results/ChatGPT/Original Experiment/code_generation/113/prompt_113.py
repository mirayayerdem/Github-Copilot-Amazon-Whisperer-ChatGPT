def odd_count(lst):
    output = []
    for i, s in enumerate(lst):
        odd_num = sum(1 for c in s if int(c) % 2 == 1)
        output.append("the number of odd elements {}n the str{}ng {} of the {}nput.".format(odd_num, odd_num, i+1, odd_num))
    return output
