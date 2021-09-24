# https://www.hackerrank.com/challenges/string-validators/problem

# In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# In the third line, print True if  has any digits. Otherwise, print False.
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

def validate_string(s):
    is_alnum = False
    is_alpha = False
    is_digit = False
    is_lower = False
    is_upper = False

    for c in s:
        if c.isalnum() == True:
            is_alnum = True
        if c.isalpha() == True:
            is_alpha = True
        if c.isdigit() == True:
            is_digit = True
        if c.islower() == True:
            is_lower = True
        if c.isupper() == True:
            is_upper = True

        # we can edn up here if all flags are already set to True:
        if is_alnum == True and is_upper == True and is_alpha == True and is_digit == True and is_lower == True:
            break
    print(is_alnum)
    print(is_alpha)
    print(is_digit)
    print(is_lower)
    print(is_upper)


if __name__ == '__main__':
    s = input()
    validate_string(s)
