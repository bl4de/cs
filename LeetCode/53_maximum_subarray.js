/*
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
    let max_sum = 0;
    let curr_sum = 0;

    for (let i of nums) {
        max_sum += i;
    }

    // time complexity: O(n^2)
    for (let k = 0; k < nums.length; k++) {
        curr_sum = 0;
        for (let i = k; i < nums.length; i++) {
            curr_sum += nums[i];
            if (curr_sum > max_sum) {
                max_sum = curr_sum;
            }
        }
    }
    return max_sum;
};

console.log(maxSubArray([-2,1,-3,4,-1,2,1,-5,4])); // 6
console.log(maxSubArray([1])); // 1
console.log(maxSubArray([-2,1])); // 1
console.log(maxSubArray([5,4,-1,7,8])); // 23


