class Solution:
    def isValid(self, s: str) -> bool:
        # 'parenthesies stack'
        p_stack = []

        # iterate over each character in string and act accordingly when
        # any of (), {} or [] is reached:
        for c in s:
            # if opening brakcet, push to p_stack
            if c in ["(", "{", "["]:
                p_stack.append(c)
            # if closing bracket:
            if c in [")", "}", "]"]:
                # if no parentesies on stack - missing opening one
                if len(p_stack) == 0:
                    return False
                # if closing ) without opening ( - wrong order
                if c == ")" and p_stack.pop() != "(":
                    return False
                # if closing } without opening { - wrong order
                if c == "}" and p_stack.pop() != "{":
                    return False
                # if closing ] without opening [ - wrong order
                if c == "]" and p_stack.pop() != "[":
                    return False
        # valid pairs should empty the stack when the last character
        # of string is reached:
        return len(p_stack) == 0  # True if no issues


s = Solution()
print(s.isValid("()"))  # True
print(s.isValid("]"))  # True
print(s.isValid("()[]{}"))  # True
print(s.isValid("{[]}"))  # True
print(s.isValid("(]"))  # False
print(s.isValid("([)]"))  # False

# True
print(s.isValid(
    "var x = function(){ console.log('test function'); let x = [123,12]; return x[0];}; x();"))

# False - missing function closing }
print(s.isValid(
    "var x = function(){ console.log('test function'); let x = [123,12]; return x[0]; x();"))

# False - missing array opening [
print(s.isValid(
    "var x = function(){ console.log('test function'); let x = 123,12]; return x[0];}; x();"))
