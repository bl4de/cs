<?php

declare(strict_types=1);

use Solution as GlobalSolution;

/**
 * Template Soultion class for LeetCode problems
 * 
 */
class Solution
{
    public function sum(int $num1, int $num2): int
    {
        return $num1 + $num2;
    }
}
// test suite
$solution = new GlobalSolution();
printf("%d", $solution->sum(10, 20));
