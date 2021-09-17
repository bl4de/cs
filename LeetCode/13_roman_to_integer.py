class Solution:

    ciphers = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        # case 1: Roman is single character
        if (len(s) == 1):
            return int(self.ciphers[s])

        num = 0
        current = ''
        prev = ''
        # case 2:
        for current in s:
            if num == 0:  # first interation: we do not have prev, so let's initialize num and set up prev:
                num += self.ciphers[current]
                prev = current
                continue
            if current == prev:
                num = num + self.ciphers[current]  # valid only for I
            else:
                if self.ciphers[current] < self.ciphers[prev]:
                    num = num + self.ciphers[current]
                else:
                    num = num - self.ciphers[prev]
                    num = num + (self.ciphers[current] - self.ciphers[prev])
            prev = current

        return num


s = Solution()

print(s.romanToInt('I'))  # 1
print(s.romanToInt('II'))  # 2
print(s.romanToInt('III'))  # 3
print(s.romanToInt('X'))  # 10
print(s.romanToInt('D'))  # 500

print(s.romanToInt('IX'))  # 9
print(s.romanToInt('XXVII'))  # 27
print(s.romanToInt('LVIII'))  # 58
print(s.romanToInt('MCMXCIV'))  # 1994
