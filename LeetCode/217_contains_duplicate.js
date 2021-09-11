/*
https://leetcode.com/problems/contains-duplicate/submissions/

Runtime: 76 ms, faster than 92.95% of JavaScript online submissions for Contains Duplicate.
Memory Usage: 44.7 MB, less than 61.27% of JavaScript online submissions for Contains Duplicate.
*/

var containsDuplicate = function (nums) {
    let n = new Set();
    for (let num of nums) {
        if (n.has(num)) {
            return true;
        }
        n.add(num);
    }
    return false;
};

console.log(containsDuplicate([1, 2, 3, 4]));

