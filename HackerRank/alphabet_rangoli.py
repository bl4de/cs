#!/usr/bin/env python3

# #size 10

# ------------------j------------------
# ----------------j-i-j----------------
# --------------j-i-h-i-j--------------
# ------------j-i-h-g-h-i-j------------
# ----------j-i-h-g-f-g-h-i-j----------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ----------j-i-h-g-f-g-h-i-j----------
# ------------j-i-h-g-h-i-j------------
# --------------j-i-h-i-j--------------
# ----------------j-i-j----------------
# ------------------j------------------

# #size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

# #size 5

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------


import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    rows = ['a' for i in range(0, (size * 2) - 1)]
    number_of_rows = size * 2 - 1
    # create middle row
    row = ''
    current_row = int(number_of_rows // 2)
    for c in range(size - 1, 0, -1):
        row += (alphabet[c] + '-')
    for c in range(0, size):
        row += (alphabet[c] + '-')
    rows[current_row] = row[:-1]
    print(rows)

    iter = 1
    while iter < current_row:
        middle_section = row[(len(row) // 2) - 3 : (len(row) // 2) + 2 ]
        middle_section_replacement = middle_section[0]
        row = middle_section_replacement
        rows[current_row + iter] = row
        rows[current_row - iter] = row
        iter += 1

    return('\n'.join(rows))

if __name__ == '__main__':

    # size = int(input())
    size = 3

    print(print_rangoli(size))
