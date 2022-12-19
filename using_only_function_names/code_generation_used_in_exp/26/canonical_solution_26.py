import collections
c = collections.Counter(numbers)
return [n for n in numbers if c[n] <= 1]
