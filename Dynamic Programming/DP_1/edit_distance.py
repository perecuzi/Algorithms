# Uses python3

def edit_distance(s, t):
    l_s = len(s) + 1
    l_t = len(t) + 1
    dis = [[x] + [0] * (l_t - 1) for x in range(l_s)]
    dis[0] = [x for x in range(l_t)]
    for i in range(1, l_s):
        for j in range(1, l_t):
            if s[i - 1] == t[j - 1]:
                dis[i][j] = dis[i - 1][j - 1]
            else:
                dis[i][j] = min(dis[i][j - 1], dis[i - 1][j], dis[i - 1][j - 1]) + 1
    return dis[-1][-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
