def calc_fib(n):
    fibonacci = [0] * (n+2)
    fibonacci[0] = 0
    fibonacci[1] = 1
    if n >= 1:
        for i in range(2, n + 1):
            fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]
    return fibonacci[n]


n = int(input())
print(calc_fib(n))