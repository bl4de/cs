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
     * solution method goes here
     * @param string $command
     * @return string
     */
    public function interpret(string $command): string
    {
        return str_replace(["()", "(al)"], ["o", "al"], $command);
    }
}

// test suite
$solution = new GlobalSolution();
$solution->solutionTest($solution->interpret("G()(al)"),  "Goal");
$solution->solutionTest($solution->interpret("G()()()()(al)"), "Gooooal");
$solution->solutionTest($solution->interpret("(al)G(al)()()G"), "alGalooG");
