#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/3sum/
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
        self.test(self.solution(
            nums=[-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
        self.test(self.solution(nums=[0, 1, 1]), [])
        self.test(self.solution(nums=[0, 0, 0]), [[0, 0, 0]])
        
        self.test(self.solution(nums=[-5,1,-10,2,-7,-13,-3,-8,2,-15,9,-3,-15,13,-6,-10,5,6,11,1,13,-12,14,6,11,4,13,-14,0,11,1,10,-11,6,-11,-10,8,2,-3,-13,-6,-9,-9,-6,11,-8,-9,1,13,9,9,3,13,0,-6,1,-10,-15,3,5,3,11,-8,0,2,-11,5,-13,6,9,-11,7,8,-13,8,4,-6,14,13,-15,1,7,-5,-1,-7,5,7,-2,-3,-13,10,7,13,9,-8,-8,13,12,-6,4,7,-10,-12,-8,-8,11,11,-6,3,9,-14,-11,2,-4,-5,10,8,-13,-7,12,-10,10]), [])

    def solution(self, nums: List[int]) -> List[List[int]]:
        """
        Solution function goes here
        """
        result = []
        l = len(nums)
        for i in range(0, l):
            for j in range(0, l):
                for k in range(0, l):
                    if i != j and j != k and k != i:
                        if nums[i] + nums[j] + nums[k] == 0:
                            r = [nums[i], nums[j], nums[k]]
                            r.sort()
                            if r not in result:
                                result.append(r)
        return result


NUMS_OF_EXECUTION = 1
SHOW_PROFILER_STATS = True

sys.setrecursionlimit(1000)
profiler = cProfile.Profile()
solution = Solution()

solution.timer_start()
profiler.enable()
for i in range(0, NUMS_OF_EXECUTION):
    profiler.run("solution.solve()")
solution.timer_stop()

if SHOW_PROFILER_STATS:
    profiler.print_stats(sort='calls')
profiler.disable()
