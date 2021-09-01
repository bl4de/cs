// sample LinkedList implementation
// 10 --> 5 --> 16

class Node {
    constructor(value) {
        this.value = value;
        this.prev = null;
        this.next = null;
    }
}

/**
 * Sample DoubleLinkedList implementation
 */
class DoubleLinkedList {

    constructor(value) {
        this.head = {
            value: value,
            prev: null,
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
        newNode.prev = this.tail;
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
        this.head.prev = newNode;
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
        const nodeAfter = node.next;

        // inser newNode:
        node.next = newNode;

        // link node after to newNode:
        newNode.next = nodeAfter;
        nodeAfter.prev = newNode;

        newNode.prev = nodeAfter.prev;

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

        nextNode.prev = prevNode;
        prevNode.next = nextNode;
        // delete nodeToRemove;
        this.length--;

        return this;
    }

    /**
     * Prinst element in the LinkedList
     */
    printList(debug = false) {
        let i = this.length;
        let node = this.head;
        do {
            console.log(node.value);
            node = node.next;
        } while (--i > 0);

        if (debug) {
            let i = this.length;
            let node = this.head;
            do {
                console.log(node);
                node = node.next;
            } while (--i > 0);
        }

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
        let direction = 'forward';
        let _iterations = 0;
        // depends on wether index is closer to beginning or end of the list:

        // @TODO: implement backward traversal right
        // if (index > this.length / 2) {
        //     node = this.tail;
        //     direction = 'backward';
        // }
        

        // iterate over nodes up to the index:
        if (direction == 'forward') {
            let iter = 0;
            while (++iter < index) {
                node = node.next;
                _iterations++;
            }
        } else {
            let iter = this.length;
            while (--iter >= index) {
                node = node.prev;
                _iterations++;
            }
        }
        console.log(`traverseToIndex(): executed ${_iterations} times}`);
        return node;
    }

}


const myDoubleLinkedList = new DoubleLinkedList(0);
myDoubleLinkedList.append(1);
myDoubleLinkedList.append(2);
myDoubleLinkedList.append(3);
myDoubleLinkedList.append(4);
myDoubleLinkedList.append(5);
myDoubleLinkedList.append(6);

// myDoubleLinkedList.printList();

myDoubleLinkedList.insert(1, 7567); // Rex
myDoubleLinkedList.insert(4, 5555); // Fives
myDoubleLinkedList.insert(7, 1409); // Echo

myDoubleLinkedList.prepend(99);
myDoubleLinkedList.printList();

myDoubleLinkedList.remove(3);
myDoubleLinkedList.insert(3, 2224); // Cody
myDoubleLinkedList.printList();

myDoubleLinkedList.remove(7);


myDoubleLinkedList.printList();
