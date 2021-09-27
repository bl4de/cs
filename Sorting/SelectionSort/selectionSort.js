// Selection Sort first implementation

const numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, 34, 54, 76, 324, 87, 334, 1, 5, 63, 87, 283, 4, 0, 34, 54, 76, 324, 87, 334];
const numbers2 = [4, 6, 8, 2, 4, 1, 9];

function selectionSort(arr) {
    let l = arr.length;
    let totalIterations = 0;

    for (let i = 0; i < l; i++) {
        // find min in arr
        let min = arr[i];
        let min_index = i;
        for (let j = i; j < l; j++) {
            if (arr[j] < min) {
                min_index = j;
                min = arr[j];
            }
            totalIterations++;
        }
        let smallest = arr[min_index];
        // move min_index value it to the beginning of arr
        arr.splice(min_index, 1);
        // remove min_index element
        arr.unshift(smallest);
    }
    console.log('passed argument array.length(): ', l, '\nexpected O(n^2): ', Math.pow(l, 2), '\nactual totalIterations: ', totalIterations);
    return arr.reverse();
}

console.log(selectionSort(numbers));
console.log(selectionSort(numbers2));

/*
passed argument array.length():  30
expected O(n^2):  900
actual totalIterations:  465
[
    0,   0,   1,  1,  2,  4,   4,   5,   5,
    6,  34,  34, 44, 54, 54,  63,  63,  76,
   76,  87,  87, 87, 87, 99, 283, 283, 324,
  324, 334, 334
]
passed argument array.length():  7
expected O(n^2):  49
actual totalIterations:  28
[
  1, 2, 4, 4,
  6, 8, 9
]
*/
