class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

/**
 * Simple Queue implementation with LinkedList
 */
class Queue {
    constructor() {
        this.first = null;
        this.last = null;
        this.length = 0;
    }

    /**
     * Peeks at first element
     * 
     * @returns {Object} first element
     */
    peek() {
        return this.first.value;
    }

    /**
     * Enqueues element in queue
     * 
     * @param {mixed} value value to be enqueued
     * @returns Instance of Queue
     */
    enqueue(value) {
        console.log(value + " enters the queue...");
        if (this.length == 0) {
            this.first = new Node(value);
            this.last = this.first;
        } else {
            const newNode = new Node(value);
            this.last.next = newNode;
            this.last = newNode;
        }
        this.length++;
        return this;
    }

    /**
     * Dequeues first element from the queue
     * 
     * @returns Dequeued element
     */
    dequeue() {
        const leavingElement = this.first;
        this.last = this.first.next ? this.last : null;
        this.first = this.first.next ? this.first.next : null;
        this.length--;
        return leavingElement;
    }

    /**
     * Returns flag is queue empty
     * 
     * @returns {Booelan} true if queue is empty, false otherwise       
     */
    isEmpty() {
        return this.length == 0;
    }
}

const myQueue = new Queue();
//Joy
//Matt
//Pavel
//Samir

myQueue.enqueue('Joy');
myQueue.enqueue('Matt');
myQueue.enqueue('Pavel');
myQueue.enqueue('Samir');

console.log(myQueue);

console.log(myQueue.dequeue().value); // -> Joy
console.log(myQueue);

console.log(myQueue.dequeue().value); // -> Matt
console.log(myQueue);

console.log(myQueue.dequeue().value); // -> Pavel
console.log(myQueue);

console.log(myQueue.dequeue().value); // -> Samir

console.log(myQueue.isEmpty());  // empty queue
console.log(myQueue);  // empty queue


