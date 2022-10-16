# Uses python3
import math
import sys


def get_majority_element(a, left, right):
    mx = 0
    j = 1
    for i in range(left + 1, right):
        if a[i] == a[mx]:
            j += 1
        else:
            j -= 1
        if j == 0:
            mx = i
            j = 1
    k = 0
    for i in range(right):
        if a[i] == a[mx]:
            k += 1
    if k > right // 2:
        return a[mx]
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))

    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
