#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/sort-array-by-increasing-frequency/description/
"""
from typing import List, Optional
import string
import sys
import cProfile
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    
    def solve(self):
        """
        Solution runner called from profiler
        """
        self.test(self.solution(nums = [1,1,2,2,2,3]), [3,1,1,2,2,2])
        self.test(self.solution(nums = [2,3,1,3,2]), [1,3,3,2,2])
        self.test(self.solution(nums = [-1,1,-6,4,5,-6,1,4,1]), [5,-1,4,4,-6,-6,1,1,1])
        

    def solution(self, nums: List[int]) -> List[int]:
        """
        Solution function goes here
        """
        occurences = {}
        result = []
        for i in nums:
            if i not in occurences.keys():
                occurences[i] = 1
            occurences[i] += 1
        print(occurences)
        return result


sys.setrecursionlimit(1000)
profiler = cProfile.Profile()
solution = Solution()

solution.timer_start()
profiler.enable()
for i in range(0, 1):
    profiler.run("solution.solve()")
solution.timer_stop()

profiler.print_stats()
profiler.disable()
