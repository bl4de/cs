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
     * @param array $candies
     * @param int $extraCandies
     * @return array
     */
    public function kidsWithCandies($candies, $extraCandies)
    {
        $kids = [];

        foreach ($candies as $kid) {
            if ($kid + $extraCandies >= max($candies)) {
                $kids[] = true;
            } else {
                $kids[] = false;
            }
        }
        return $kids;
    }
}
// test suite
$solution = new GlobalSolution();
var_dump($solution->kidsWithCandies([2, 3, 5, 1, 3], 3));
var_dump($solution->kidsWithCandies([4, 2, 1, 1, 2], 1));
