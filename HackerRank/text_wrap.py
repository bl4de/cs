# https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap

def wrap(string, max_width):
    wrapped = ''
    iter = 0
    while iter < len(string):
        wrapped = wrapped + string[iter:iter + max_width] + '\n'
        iter += max_width

    return wrapped


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
