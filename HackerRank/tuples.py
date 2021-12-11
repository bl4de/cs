from typing import Tuple


if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))

    t = ()

    for i in range(0, n):
        t = t + (integer_list[i],)

    print(t)
    print(hash(t))
    print(hash(t) == 3713081631934410656)
