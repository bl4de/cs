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
     * @param string $s
     * @return bool
     */
    public function checkZeroOnes(string $s): bool
    {
        $longestZeroes = 0;
        $currentZeroes = 0;
        $longestOnes = 0;
        $currentOnes = 0;

        foreach (str_split($s) as $c) {
            if ($c == '1') {
                $currentOnes++;
                $currentZeroes = 0;
            } else {
                $currentZeroes++;
                $currentOnes = 0;
            }
            $longestOnes = ($currentOnes > $longestOnes) ? $currentOnes : $longestOnes;
            $longestZeroes = ($currentZeroes > $longestZeroes) ? $currentZeroes : $longestZeroes;
        }
        return $longestOnes > $longestZeroes;
    }
}
// test suite
$solution = new GlobalSolution();
$solution->solutionTest($solution->checkZeroOnes("1101"), true);
$solution->solutionTest($solution->checkZeroOnes("111000"), false);
$solution->solutionTest($solution->checkZeroOnes("110100010"), false);
$solution->solutionTest($solution->checkZeroOnes("01111110"), true);
