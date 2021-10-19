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

def create_line(line_length, middle_elements):
    line = ''
    mel = '.|.'

    line = '-' * ((line_length - middle_elements * len(mel))//2)
    line += mel * middle_elements
    line += '-' * ((line_length - middle_elements * len(mel))//2)

    return line


def create_mat(mat_high):
    welcome = 'WELCOME'
    mat_width = mat_high * 3
    mat = []
    middle_elements = 1

    for iter in range(0, mat_high//2):
        mat.append(create_line(mat_width, middle_elements))
        middle_elements += 2

    line = '-' * ((mat_width - len(welcome)) // 2
                  + (0 if mat_width % 2 != 0 else 1)) \
        + welcome \
        + '-' * ((mat_width - len(welcome)) // 2 +
                 (0 if mat_width % 2 != 0 else 1))

    mat.append(line)
    middle_elements -= 2

    for iter in range(mat_high//2 - 1, -1, -1):
        mat.append(create_line(mat_width, middle_elements))
        middle_elements -= 2

    print('\n'.join(mat))


if __name__ == '__main__':
    # mat_high = int(input())

    mat_high, mat_width = input().split()
    if int(mat_high) > 0:
        create_mat(int(mat_high))
