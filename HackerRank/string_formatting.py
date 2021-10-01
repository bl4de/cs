# https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    spaces = len(bin(number)) - 1
    for n in range(1, number + 1):
        print(f"%{spaces-1}d%{spaces}o%{spaces}s%0{spaces}s" % (n, n, hex(n).upper()[2:], bin(n)[2:]))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
