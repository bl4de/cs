/**
 * @param {Object | Array} obj
 * @return {boolean}
 */
var isEmpty = function (obj) {
    if (Array.isArray(obj)) {
        return obj.length === 0;
    } else {
        return Object.keys(obj).length === 0;
    }
    return true;
};

console.log(isEmpty({}));
console.log(isEmpty({ "key": "val" }));

console.log(isEmpty([]));
console.log(isEmpty([1, 2, 3]));
