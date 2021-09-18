class Solution:
    def longestCommonPrefix(self, strs) -> str:
        shortest = len(strs[0]) # initial shortest string
        self.lcp = ""
        self.iters = 0

        print("\nnumber of strings: {}".format(len(strs)))
        # find the shortest string:
        # this is max how many times we have to iterate:
        # also, if any string is empty, return immediately
        for s in strs:
            if len(s) == 0:
                return self.lcp
            else:
                if len(s) < shortest:
                    shortest = len(s)

        print("-> shortest string len: {} | O() time complexity worst case scenario: {} "
            .format(shortest, len(strs) * shortest))
        # iterate over each string character by character <= longest
        # if each str[iteration] is the same, iterate again
        # if not - break loop and return
        # self.lcp found so far (or "" if not found)
        for loop in range(0, shortest):
            c = strs[0][loop]
            for iter in range(1, len(strs)):
                self.iters += 1
                if strs[iter][loop] != c:
                    return "Longest Common Prefix found: {}".format(self.lcp)
            self.lcp += c

        return self.lcp

    def iters_counter(self):
        print("-> total no. of interations: {}\n\n".format(self.iters))


s = Solution()

print(s.longestCommonPrefix(["flower", "flow", "flight"]))  # "fl"
s.iters_counter()

print(s.longestCommonPrefix(["dog", "racecar", "car"]))  # ""
s.iters_counter()

print(s.longestCommonPrefix(["anabel", "analfabeta", "anacron"]))  # "ana"
s.iters_counter()

print(s.longestCommonPrefix(["Audi", "Apple", "Amazon"]))  # "A"
s.iters_counter()

print(s.longestCommonPrefix(["", "b"]))  # ""
s.iters_counter()

print(s.longestCommonPrefix(["ab", "a"]))  # "a"
s.iters_counter()
