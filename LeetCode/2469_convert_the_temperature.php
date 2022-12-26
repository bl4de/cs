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
     * @param Float $celsius
     * @return Float[]
     */
    public function convertTemperature(Float $celsius): array
    {
        return [
            $celsius + 273.15,
            $celsius *  1.80 + 32.00
        ];
    }
}
// test suite
$solution = new GlobalSolution();
$solution->solutionTest($solution->convertTemperature(36.50), [309.65000, 97.70000]);
$solution->solutionTest($solution->convertTemperature(122.11), [395.26000, 251.79800]);
