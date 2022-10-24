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
     * @param String $sentence
     * @return Integer
     */
    public function countValidWords($sentence)
    {
        return 0;
    }
}
// test suite
$solution = new GlobalSolution();
echo ($solution->countValidWords("cat and  dog")); // 3
echo ($solution->countValidWords("!this  1-s b8d!")); // 0
echo ($solution->countValidWords("alice and  bob are playing stone-game10")); // 5
