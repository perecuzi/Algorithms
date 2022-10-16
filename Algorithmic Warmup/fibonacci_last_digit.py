def calc_fib(n):
    fibonacci = [0] * (n+1)
    fibonacci[0] = 0
    fibonacci[1] = 1
    for i in range(2, n+1):
        fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
    return fibonacci


def find_last_digit(n):
    f = [0] * 61
    f = calc_fib(60)
    return f[n % 60] % 10


n = int(input())
print(find_last_digit(n))


