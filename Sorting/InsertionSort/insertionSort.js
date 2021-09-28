const numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];

function insertionSort(arr) {
    let l = arr.length;
    let tmp;
    let numberOfIterations = 0;

    for (let j = 0; j < l; j++) {
        let i = 1;
        while (arr[i] < arr[i - 1]) {
            tmp = arr[i - 1];
            arr[i - 1] = arr[i];
            arr[i] = tmp;
            i++;
            numberOfIterations++;
        }
    }
    console.log('total iterations: ', numberOfIterations);
}

insertionSort(numbers);
console.log(numbers);
