/**
 * Simple Stack implementation with Array
 */
class Stack {
    /**
     * Creates new instance of Stack
     */
    constructor() {
        this.stack = [];
        return this;
    }

    /**
     * Shows the value on top of the stack without removing it
     */
    peek() {
        if (this.stack.length > 0) {
            console.log("Top: ", this.stack[this.stack.length - 1]);
        }
        return null;
    }

    /**
     * Pushes value on top of the stack
     * 
     * @param {mixed} value value to push on stack
     */
    push(value) {
        this.stack.push(value);
    }

    /**
     * Pops value from top of the stack
     * 
     * @returns {mixed}
     */
    pop() {
        return this.stack.pop();
    }

    /**
     * Returns wether stack is empty or not
     * 
     * @returns {Boolean}
     */
    isEmpty() {
        return this.stack.length === 0;
    }

    /**
     * Prints stack
     */
    printStack() {
        console.log('\n_____bottom_____');
        for (let _element of this.stack) {
            console.log(_element);
        }
        console.log('____top____\n');
    }
}

const myStack = new Stack();


myStack.peek();

myStack.push('google');
myStack.push('salesforce');
myStack.push('facebook');
myStack.push('yahoo');
myStack.push('ibm');

myStack.printStack();

console.log(myStack.pop());
console.log(myStack.pop());

myStack.printStack();
myStack.peek();

console.log(myStack.pop());
myStack.printStack();

console.log(myStack.isEmpty());
