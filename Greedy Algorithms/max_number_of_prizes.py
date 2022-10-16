# Uses python3
import sys


def optimal_summands(n):
    summands = []
    total_remaining = n
    total_added = 0
    for i in range(1, n+1, 1):
        if total_remaining - i > i:
            total_added += i
            total_remaining -= i
            summands.append(i)
        if total_remaining - i == 0:
            summands.append(total_remaining)
            return summands
    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
