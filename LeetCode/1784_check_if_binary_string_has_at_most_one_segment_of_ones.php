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
     * Test cases
     * 
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
     * 
     */
    public function solution()
    {
    }
}
// test suite
$solution = new GlobalSolution();
