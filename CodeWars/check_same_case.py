# Write a function that will check if two given characters are the same case.
# 'a' and 'g' returns 1
# 'A' and 'C' returns 1
# 'b' and 'G' returns 0
# 'B' and 'g' returns 0
# '0' and '?' returns -1
# If any of characters is not a letter, return -1.
# If both characters are the same case, return 1.
# If both characters are letters and not the same case, return 0.

def assert_equals(fn, result):
    print((fn == result) == True)


def same_case(a, b):
    # your code here
    pass


assert_equals(same_case('C', 'B'), 1)
assert_equals(same_case('b', 'a'), 1)
assert_equals(same_case('d', 'd'), 1)
assert_equals(same_case('A', 's'), 0)
assert_equals(same_case('c', 'B'), 0)
assert_equals(same_case('b', 'Z'), 0)
assert_equals(same_case('\t', 'Z'), -1)
assert_equals(same_case('H', ':'), -1)
