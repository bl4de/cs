const numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];

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

    console.log('total iterations: ', numberOfIterations);
}

bubbleSort(numbers);
console.log(numbers);
