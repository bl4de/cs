const numbers = [99, 44, 6, 88, 2, 1, 5, 92, 87];
const numbers2 = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];

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
            }
            numberOfIterations++;
        }
    }
    console.log('total iterations: ', numberOfIterations);
}

insertionSort(numbers);
insertionSort(numbers2);
console.log(numbers);
console.log(numbers2);
