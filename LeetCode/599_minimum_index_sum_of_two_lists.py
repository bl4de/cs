#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        """
        Solution function goes here
        """
        result = []
        return result


sys.setrecursionlimit(1000)
solution = Solution()

solution.test(solution.findRestaurant(list1=["Shogun", "Tapioca Express", "Burger King", "KFC"], list2=[
              "Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]), ["Shogun"])
solution.test(solution.findRestaurant(list1=["Shogun", "Tapioca Express", "Burger King", "KFC"], list2=[
              "KFC", "Shogun", "Burger King"]), ["Shogun"])
solution.test(solution.findRestaurant(list1=["happy", "sad", "good"], list2=[
              "sad", "happy", "good"]), ["sad", "happy"])

# solution.timer_start()
# for i in range(0, 1000000):
#     pass
# solution.timer_stop()
