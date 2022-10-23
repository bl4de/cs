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
     * @param array $sentences
     * @return int
     */
    public function mostWordsFound(array $sentences): int
    {
        $max = 0;
        foreach ($sentences as $sentence) {
            $words = count(explode(" ", $sentence));
            $max = ($words > $max) ? $words : $max;
        }
        return $max;
    }
}
// test suite
$solution = new GlobalSolution();

echo ($solution->mostWordsFound([
    "alice and bob love leetcode",
    "i think so too",
    "this is great thanks very much"
])); // 6
