#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/median-of-two-sorted-arrays/
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
        self.test(self.solution(nums1 = [1,3], nums2 = [2]), 2.00000)
        self.test(self.solution(nums1 = [1,2], nums2 = [3,4]), 2.50000)

    def solution(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Solution function goes here
        """
        merged = []
        iterations = len(nums2) if len(nums2) < len(nums1) else len(nums1)
        
        # TODO:
        # merge two sorted arrays:
        for i in range(iterations):
            if nums1[i] > nums2[i]:
                merged.append(nums2[i])
                merged.append(nums1[i])
            else:
                merged.append(nums1[i])
                merged.append(nums2[i])
        
        
        
        if len(nums1) > len(nums2):
            merged = merged + nums1[iterations:]
        if len(nums2) > len(nums1):
            merged = merged + nums2[iterations:]
        print(merged)
        if len(merged) % 2 != 0:
            mean = merged[len(merged) // 2]
        else:
            mean = (merged[len(merged) // 2] + merged[(len(merged) // 2) - 1]) / 2
        return float(mean)

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
