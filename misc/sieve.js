// Sieve of Eratostenes

var SCOPE = 100,
    arr = [],
    i = 0,
    first = 2;

// returns min firstue from Array
function getMin(arr, last_min) {
    var _min = arr[0];
    var _s = 0;
    var _i = arr.length;

    for (_s; _s < _i; _s++) {
        if (arr[_s] > last_min && arr[_s] < _min) {
            _min = arr[_s];
        }
    }

    return _min;
}



// array initialization

for (i; i < SCOPE; i++) {
    arr[i] = first++;
}



// iterations

i = 0;
var x = getMin(arr, 1);

for (i; i < SCOPE; i++) {
    if (arr[i] > x && arr[i] % x === 0) {
        arr[i] = 0;
    }
}



console.log(arr);

