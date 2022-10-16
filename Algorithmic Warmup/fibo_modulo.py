def calc_fib(n):
    fibonacci = [0] * (n + 2)
    fibonacci[0] = 0
    fibonacci[1] = 1
    if n >= 1:
        for i in range(2, n + 1):
            fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]
    return fibonacci[n]


def pisano_period(m):
    previous = 0
    current = 1
    for i in range(0, m * m):
        previous, current \
            = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i + 1


def fibo_modulo(x, y):
    v = x % pisano_period(y)
    return calc_fib(v) % y



if __name__ == "__main__":
    a, b = map(int, input().split())
    print(fibo_modulo(a, b))
