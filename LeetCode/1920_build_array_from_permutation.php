<?php

declare(strict_types=1);

use Solution as GlobalSolution;

/**
 * Template Soultion class for LeetCode problems
 * 
 */
class Solution
{
    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    public function buildArray(array $nums): array
    {
        $ans = [];
        foreach ($nums as $i) {
            $ans[$i] = $nums[$i];
        }
        return $ans;
    }
}
// test suite
$solution = new GlobalSolution();
print_r($solution->buildArray([0, 2, 1, 5, 3, 4])); // [0,1,2,4,5,3]
print_r($solution->buildArray([5, 0, 1, 2, 3, 4])); // [4,5,0,1,2,3]
