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
        common_strings = {}
        min_occurence = len(list1) if len(list1) > len(list2) else len(list2)
        for s in list1:
            if s in list2:
                common_strings[s] = list1.index(s) + list2.index(s)
                min_occurence = (list1.index(s) + list2.index(s)) if (
                    list1.index(s) + list2.index(s)) < min_occurence else min_occurence
        for common_string, occurence in common_strings.items():
            if occurence == min_occurence:
                result.append(common_string)

        return result


sys.setrecursionlimit(1000)
solution = Solution()

solution.test(solution.findRestaurant(list1=["Shogun", "Tapioca Express", "Burger King", "KFC"], list2=[
              "Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]), ["Shogun"])
solution.test(solution.findRestaurant(list1=["Shogun", "Tapioca Express", "Burger King", "KFC"], list2=[
              "KFC", "Shogun", "Burger King"]), ["Shogun"])
solution.test(solution.findRestaurant(list1=["happy", "sad", "good"], list2=[
              "sad", "happy", "good"]), ["sad", "happy"])
