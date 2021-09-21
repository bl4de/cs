// Write two functions that finds the factorial of any number. 
// One should use recursive, the other should just use a for loop

/**
 * Factorial via recursion
 * 
 * Time complexity: O(n)
 * 
 * @param {number} number 
 * @returns number
 */
function findFactorialRecursive(number) {
    if (number == 1) {
        return number;
    } else {
        return number * findFactorialRecursive(number - 1);
    }
}

/**
 * Factorial via loop
 * 
 * Time complexity: O(n)
 * 
 * @param {number} number 
 * @returns number
 */
function findFactorialIterative(number) {
    if (number == 1) {
        return number;
    }
    let answer = 1;
    for (let iter = 2; iter <= number; iter++) {
        answer = answer * iter;
    }
    return answer;
}


console.log(findFactorialRecursive(3));// 6
console.log(findFactorialRecursive(5));// 120
console.log(findFactorialRecursive(6));// 720
console.log(findFactorialRecursive(7));// 5040

console.log(findFactorialIterative(3));// 6
console.log(findFactorialIterative(5));// 120
console.log(findFactorialIterative(6));// 720
console.log(findFactorialIterative(7));// 5040


