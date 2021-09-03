class Node {
    constructor(value) {
        this.value = value;
        this.prev = null;
    }
}

/**
 * Simple Stack implementation with LinkedList
 */
class Stack {
    /**
     * Creates new instance of Stack
     */
    constructor() {
        this.top = null;
        this.bottom = null;
        this.length = 0;
    }

    /**
     * Shows the value on top of the stack without removing it
     */
    peek() {
        console.log("Top: ", this.top.value);
    }

    /**
     * Pushes value on top of the stack
     * 
     * @param {mixed} value value to push on stack
     */
    push(value) {
        const newNode = new Node(value);
        newNode.prev = this.top;
        this.top = newNode;
        this.length++;
    }

    /**
     * Pops value from top of the stack
     * 
     * @returns {mixed}
     */
    pop() {
        if (this.length > 0) {
            let _t = this.top;
            this.top = this.top.prev;
            this.length--;
            return _t;
        }
        return null;
    }

    /**
     * Returns wether stack is empty or not
     * 
     * @returns {Boolean}
     */
    isEmpty() {
        return this.length === 0;
    }

    /**
     * Prints stack
     */
    printStack() {
        let _element = this.top;
        let _iter = this.length;

        console.log("\n____top________");
        while (_iter) {
            console.log(_element.value);
            _element = _element.prev;
            _iter--;
        }
        console.log('_____bottom_____');
    }
}

const myStack = new Stack();

myStack.push('google');
myStack.push('salesforce');
myStack.push('facebook');
myStack.push('yahoo');
myStack.push('ibm');

myStack.printStack();

console.log(myStack.pop().value);
console.log(myStack.pop().value);

myStack.printStack();
myStack.peek();

console.log(myStack.pop());
console.log(myStack.isEmpty());
