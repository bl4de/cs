// sample LinkedList implementation
// 10 --> 5 --> 16

class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

/**
 * Sample LinkedList implementation
 */
class LinkedList {

    constructor(value) {
        this.head = {
            value: value,
            next: null
        };
        this.tail = this.head;
        this.length = 1;
        return this;
    }

    /**
     * Appends element at the end of the LinkedList
     * 
     * @param {mixed} value Value to append to
     * @returns {this} LinkedList instance 
     */
    append(value) {
        const newNode = new Node(value);
        this.tail.next = newNode;
        this.tail = newNode;
        this.length++;
        return this;
    }

    /**
     * Prepends LinkedList with element of value = value
     * 
     * @param {mixed} value Value to insert at the beginning of the list
     * @returns {Object} LinkedList instance
     */
    prepend(value) {
        const newNode = new Node(value);
        newNode.next = this.head;
        this.head = newNode;
        this.length++;

        return this;
    }

    /**
     * Inserts element of value = value at index = index
     * 
     * @param {Number} index index where to insert new node
     * @param {mixed} value value to insert
     * @returns {Object} LinkedList instance
     */
    insert(index, value) {
        if (index < 0 || index >= this.length) {
            return this.append(value);
        }

        // if index equals 0 - it's just prepend()
        if (index === 0) {
            return this.prepend(value);
        }

        // if index equals last element - it's just append()
        if (index === this.length - 1) {
            return this.append(value);
        }

        const newNode = new Node(value);
        let node = this.traverseToIndex(index);

        // get reference to node which will be linked from newNode:
        nodeAfter = node.next;

        // inser newNode:
        node.next = newNode;

        // link node after to newNode:
        newNode.next = nodeAfter;

        this.length++;

        return this;
    }

    /**
     * Removes node at position index
     * 
     * @param {Number} index index
     * @returns {Object}
     */
    remove(index) {
        if (index < 0 || index >= this.length) {
            return this;
        }

        let prevNode = this.traverseToIndex(index);
        let nodeToRemove = prevNode.next;
        let nextNode = nodeToRemove.next;

        prevNode.next = nextNode;
        // delete nodeToRemove;
        this.length--;

        return this;
    }

    /**
     * Prinst element in the LinkedList
     */
    printList() {
        let i = this.length;
        let node = this.head;
        console.log("\n\n");
        do {
            console.log(node.value);
            node = node.next;
        } while (--i > 0);
        return this;
    }

    /**
     * Traverses LinkedList up to index and returns node
     * with this index.
     * 
     * @param {Number} index node index
     * @returns {Object} node
     */
    traverseToIndex(index) {
        let node = this.head;
        let iter = 0;

        // iterate over nodes up to the index:
        while (++iter < index) {
            node = node.next;
        }

        return node;
    }

    /**
     * Reverse LinkedList
     */
    reverse() {
        if (!this.head.next) {
            return this;
        }
        let first = this.head;
        this.tail = this.head;
        let second = first.next;

        while (second) {
            const temp = second.next;
            second.next = first;
            first = second;
            second = temp;
        }
        this.head.next = null;
        this.head = first;

        this.printList();
        return this;
    }
}


const myLinkedList = new LinkedList(0);
myLinkedList.append(1);
myLinkedList.append(2);
myLinkedList.append(3);
myLinkedList.append(4);
myLinkedList.append(5);
myLinkedList.append(6);
myLinkedList.append(7);
myLinkedList.append(8);

// myLinkedList.insert(5, 7567);

// myLinkedList.remove(3);
// myLinkedList.remove(3);
// myLinkedList.remove(3);
// myLinkedList.remove(7);


myLinkedList.printList();

myLinkedList.reverse();




