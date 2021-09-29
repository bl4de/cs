const numbers = [99, 44, 6, 88, 2, 1, 5, 92, 87]; // random
const numbers2 = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]; // random
const numbers3 = [2, 1, 3, 4, 6, 5, 7, 8, 9]; // almost sorted
const numbers4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]; // sorted

function insertionSort(arr) {
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
    console.log('total iterations: ', numberOfIterations);
}

insertionSort(numbers);
console.log(numbers);

insertionSort(numbers2);
console.log(numbers2);

insertionSort(numbers3);
console.log(numbers3);

insertionSort(numbers4);
console.log(numbers4);
