# Uses python3
import sys
import random


def partition3(a, la, r):
    ax = a[la]
    rt = r
    i = la
    while i <= rt:
        if a[i] < ax:
            a[i], a[la] = a[la], a[i]
            la += 1
            i += 1
        elif a[i] > ax:
            a[i], a[rt] = a[rt], a[i]
            rt -= 1
        else:
            i += 1
    return la, rt


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    # use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
