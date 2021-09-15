/*
    Given a signed 32-bit integer x, return x with its digits reversed. 
    If reversing x causes the value to go outside 
    the signed 32-bit integer range [-231, 231 - 1], then return 0.
*/

/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
    let signed = (x < 0) ? true : false;
    x = Math.abs(x).toString();
    reversed = [];
    for (let c of x) {
        reversed.push(c);
    }
    reversed = parseInt(reversed.reverse().join(''),10);
    if (reversed > (Math.pow(2,31) - 1) || reversed < Math.pow(-2, 31)) {
        return 0;
    }
    return (signed) ? -reversed : reversed;
};

console.log(reverse(123)); // 321
console.log(reverse(-123)); // -321
console.log(reverse(120)); // 21
console.log(reverse(1534236469)); // 0
console.log(reverse(0)); // 0

