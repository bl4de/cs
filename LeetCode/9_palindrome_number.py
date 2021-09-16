def is_palindrome(num: int) -> bool:
    return str(num) == ''.join(list(reversed(str(num))))


print(is_palindrome(121))  # True
print(is_palindrome(-121))  # False
print(is_palindrome(10))  # False
