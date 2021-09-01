/* jshint strict: true */
/* global console */


function Stack() {
    "use strict";

    var top = null,
        count = 0;

    //Returns the number of items in the queue
    this.GetCount = function () {
        return count;
    };

    /* Methods */
}



var stack = new Stack();


console.log(stack.GetCount());


console.log(stack);