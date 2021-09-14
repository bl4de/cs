/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
// first solution: time complexity -> O(n^2)
var twoSum = function (nums, target) {
    
    for (let i = 0; i < nums.length; i++) {
        for (let j = 1; j < nums.length; j++) {
            if (i !== j && nums[i] + nums[j] === target) {
                return [i, j];
            }
        }
    }
    return [];
};

console.log(twoSum([2, 7, 11, 15], 9)); // [0,1]
console.log(twoSum([3, 2, 4], 6)); // [1,2]
console.log(twoSum([3, 3], 6)); // [0,1]
console.log(twoSum([2,5,5,11], 10)); // [1,2]

