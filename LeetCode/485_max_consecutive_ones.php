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
     * test cases
     * @param mixed $input
     * @param mixed $expectedOutput
     */
    public function solutionTest(mixed $input, mixed $expectedOutput): void
    {
        if ($input !== $expectedOutput) {
            echo "[-] FAIL -> ";
        } else {
            echo "[+] PASS -> ";
        }
        print_r($input);
        echo " : ";
        print_r($expectedOutput);
        echo "\n";
    }

    /** 
     * @param Integer[] $nums
     * @return Integer
     */
    public function findMaxConsecutiveOnes(array $nums): int
    {
        if (count($nums) == 1) {
            return (int)$nums[0];
        }
        $max_c = 0;
        $current_c = 0;
        foreach ($nums as $num) {
            if ($num == '1') {
                $current_c++;
                if ($current_c > $max_c) {
                    $max_c = $current_c;
                }
            } else {
                $current_c = 0;
            }
        }
        return $max_c;
    }
}
// test suite
$solution = new GlobalSolution();
$solution->solutionTest($solution->findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]), 3);
$solution->solutionTest($solution->findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]), 2);
$solution->solutionTest($solution->findMaxConsecutiveOnes([0]), 0);
$solution->solutionTest($solution->findMaxConsecutiveOnes([1]), 1);
