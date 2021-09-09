/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    nums.forEach( n => nums.push(n));
    return nums;
};

console.log(getConcatenation([1,2,1]));
