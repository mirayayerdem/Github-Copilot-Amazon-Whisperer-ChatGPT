

def prime_fib(n: int):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def fib(n):
        fib_list = [0, 1]
        for i in range(2, n+1):
            fib_list.append(fib_list[i-1] + fib_list[i-2])
        return fib_list

    fib_list = fib(n)
    prime_fib = []
    for i in fib_list:
        if is_prime(i):
            prime_fib.append(i)
    return prime_fib
