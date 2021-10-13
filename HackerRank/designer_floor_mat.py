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
    welcome = 'WELCOME'
    mat_width = mat_high * 3
    center = mat_width//2
    mat = []

    for iter in range(0, mat_high//2):
        line = '-' * (center - iter) + \
            '.' * (iter + 1) + \
            '|' + \
            '.' * (iter + 1) + \
            '-' * (center - iter)
        mat.append(line)

    line = '-' * ((mat_width - len(welcome)) // 2
                  + (1 if mat_width % 2 != 0 else 2)) \
        + welcome \
        + '-' * ((mat_width - len(welcome)) // 2 +
                 (1 if mat_width % 2 != 0 else 2))

    mat.append(line)
    for iter in range(mat_high//2 - 1, -1, -1):
        line = '-' * (center - iter) + '.' * (iter + 1) + '|' + \
            '.' * (iter + 1) + '-' * (center - iter)
        mat.append(line)

    print('\n'.join(mat))


if __name__ == '__main__':
    # mat_high = int(input())

    mat_high = 7
    if mat_high > 0:
        create_mat(mat_high)

    exit(0)
