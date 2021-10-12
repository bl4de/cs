# https://www.hackerrank.com/challenges/designer-door-mat/problem

# SAMPLES:
#
# Size: 7 x 21
# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME-------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------

# Size: 11 x 33
# ---------------.|.---------------
# ------------.|..|..|.------------
# ---------.|..|..|..|..|.---------
# ------.|..|..|..|..|..|..|.------
# ---.|..|..|..|..|..|..|..|..|.---
# -------------WELCOME-------------
# ---.|..|..|..|..|..|..|..|..|.---
# ------.|..|..|..|..|..|..|.------
# ---------.|..|..|..|..|.---------
# ------------.|..|..|.------------
# ---------------.|.---------------


def create_mat(mat_high):
    mat_width = mat_high * 3
    center = mat_width//2
    mat = []
    for iter in range(0, mat_high):
        line = '-' * (center - iter) + '.' * (iter + 1) + '|' + \
            '.' * (iter + 1) + '-' * (center - iter)
        mat.append(line)

    welcome = 'WELCOME'
    # print(welcome)
    print('\n'.join(mat))
    pass


if __name__ == '__main__':
    # mat_high = int(input())

    mat_high = 7

    if mat_high > 0:
        create_mat(mat_high)

    exit(0)
