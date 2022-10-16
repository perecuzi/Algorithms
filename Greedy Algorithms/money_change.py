def get_change(m):
    count = m // 10
    a = m % 10
    if a >= 5:
        count += a // 5
        count += a % 5
    else:
        count += m % 10

    return count


if __name__ == '__main__':
    b = int(input())
    print(get_change(b))
