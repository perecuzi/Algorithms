# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.
    for i in range(n - 1, -1, -1):
        if capacity == 0:
            return value
        a = min(weights[i], capacity)
        value += a * (values[i] / weights[i])
        capacity -= a
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, cap = data[0:2]
    i_values = data[2:(2 * n + 2):2]
    i_weights = data[3:(2 * n + 2):2]
    vw = [0] * n
    for k in range(n):
        vw[k] = i_values[k] / i_weights[k]
    vw, i_values, i_weights = zip(*sorted(zip(vw, i_values, i_weights)))
    opt_value = get_optimal_value(cap, list(i_weights), list(i_values))
    print("{:.4f}".format(opt_value))
