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
     * @var int $hw
     */
    private int $hw = 0;

    /**
     * @param int $n
     * @return int
     */
    public function hammingWeight(int $n): int
    {
        $this->hw = 0;
        for ($i = 0; $i < 32; $i++) {
            if ($n & pow(2, $i)) {
                $this->hw++;
            }
        }
        return $this->hw;
    }
}
// test suite
$solution = new GlobalSolution();
printf("%d\n", $solution->hammingWeight(0b00000000000000000000000000001011)); // 3
printf("%d\n", $solution->hammingWeight(0b00000000000000000000000010000000)); // 1
printf("%d\n", $solution->hammingWeight(0b11111111111111111111111111111101)); // 31
