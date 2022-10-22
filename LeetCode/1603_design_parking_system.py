#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
'''
    LeetCode solution class
'''
from typing import List, Optional


class Solution:
    '''
    LeetCode solution class
    '''

    def __init__(self, big: int, medium: int, small: int):
        self.parking = {
            "1": big,
            "2": medium,
            "3": small
        }

    def addCar(self, carType: int) -> bool:
        '''
        Parks the car
        '''
        is_available = self.parking[str(carType)] > 0
        self.parking[str(carType)] = self.parking[str(carType)] - 1
        return is_available


solution = Solution(1, 1, 0)
print(solution.addCar(1))
print(solution.addCar(2))
print(solution.addCar(3))
print(solution.addCar(1))
