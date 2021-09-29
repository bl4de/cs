const numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];
const numbers3 = [2, 1, 3, 4, 6, 5, 7, 8, 9]; // almost sorted
/**
 * Bubble Sort very naive implementation
 * time complexity - O(n^2)
 * 
 * @param {Array} array Arrya to sort
 * @returns Array
 */
function bubbleSort(array) {
    let tmp;
    let numberOfIterations = 0;

    for (let i = 0; i < array.length - 1; i++) {
        for (let iter = 0; iter < array.length - 1; iter++) {
            if (parseInt(array[iter]) > parseInt(array[iter + 1])) {
                tmp = array[iter + 1];
                array[iter + 1] = array[iter];
                array[iter] = tmp;
            }
            numberOfIterations++;
        }
    }

    // console.log('total iterations: ', numberOfIterations);
}


console.time('bubbleSort');
for (let i = 0; i < 1000000; i++) {
    bubbleSort(numbers); // -> 32 iterations
}
console.log(numbers);
console.timeEnd('bubbleSort');