/**
 * @param {number} x
 * @return {boolean}
 */

// first submission - very slow, a lot of memory consumed
var isPalindrome_1 = function(x) {
    pal = true;
    s = x.toString();
    for (let iter = 0; iter <= (s.length/2); iter++) {
        if (s[iter] !== s[(s.length - iter) - 1]) {
            pal = false;
        }
    }
    return pal;
};

// second solution - little bit faster, but still sloooow...
// very memory efficient (less than ~90% of all submissions)
var isPalindrome = function(x) {
    let s = Array.from(x.toString());
    let rs = [...s].reverse();
    return s.join('') == rs.join('');
};


