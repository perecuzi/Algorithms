def gcd(ax, bx):
    while bx > 0:
        ay = bx
        by = ax % bx
        ax = ay
        bx = by
    current_gcd = ax

    return current_gcd


def lcm(m, n):
    l_c_m = (m * n) / gcd(m, n)
    return int(l_c_m)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(lcm(a, b))
