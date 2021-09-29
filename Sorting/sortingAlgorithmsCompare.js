const numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, 34, 54, 76, 324, 87, 334, 1, 5, 63, 87, 283, 4, 0, 34, 54, 76, 324, 87, 334]; // random
const numbers3 = [2, 1, 3, 4, 6, 5, 7, 8, 9]; // almost sorted
const numbers4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]; // sorted

// my insertionSort implementation
function myInsertionSort(arr) {
    let l = arr.length;
    let tmp;
    let numberOfIterations = 0;

    for (let j = 0; j <= l; j++) {
        let i = 0;
        while (i < l) {
            if (arr[i] > arr[i + 1]) {
                tmp = arr[i + 1];
                arr[i + 1] = arr[i];
                arr[i] = tmp;
                i++;
            } else {
                i++;
                continue;
            }
            numberOfIterations++;
        }
    }
    // console.log('total iterations: ', numberOfIterations);
}


// solution from the course -> https://replit.com/@aneagoie/insertionSort
function insertionSort(array) {
    const length = array.length;
    for (let i = 0; i < length; i++) {
        if (array[i] < array[0]) {
            //move number to the first position
            array.unshift(array.splice(i, 1)[0]);
        } else {
            // only sort number smaller than number on the left of it. This is the part of insertion sort that makes it fast if the array is almost sorted.
            if (array[i] < array[i - 1]) {
                //find where number should go
                for (var j = 1; j < i; j++) {
                    if (array[i] >= array[j - 1] && array[i] < array[j]) {
                        //move number to the right spot
                        array.splice(j, 0, array.splice(i, 1)[0]);
                    }
                }
            }
        }
    }
}

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
}

// my selectionSort implementation
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
    return arr.reverse();
}

const NUMBER_OF_ITERATIONS = 1000000;

console.time('bubbleSort');
for (let i = 0; i < NUMBER_OF_ITERATIONS; i++) {
    bubbleSort(numbers);
}
console.log(numbers);
console.timeEnd('bubbleSort');

console.time('insertionSort');
for (let i = 0; i < NUMBER_OF_ITERATIONS; i++) {
    insertionSort(numbers);
}
console.log(numbers);
console.timeEnd('insertionSort');


console.time('myInsertionSort');
for (let i = 0; i < NUMBER_OF_ITERATIONS; i++) {
    myInsertionSort(numbers);
}
console.log(numbers);
console.timeEnd('myInsertionSort');

console.time('selectionSort');
for (let i = 0; i < NUMBER_OF_ITERATIONS; i++) {
    selectionSort(numbers);
}
console.log(numbers);
console.timeEnd('selectionSort');
