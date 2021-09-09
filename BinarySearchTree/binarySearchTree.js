// helper function for traverse the Tree
function traverse(node) {
    const tree = { value: node.value };
    tree.left = node.left === null ? null : traverse(node.left);
    tree.right = node.right === null ? null : traverse(node.right);
    return tree;
}


/**
 * Helper class to create BST Node
 */
class Node {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

/**
 * Simple Binary Search Tree implementation
 */
class BinarySearchTree {

    /**
     * Constructor
     */
    constructor() {
        this.root = null;
        this.notFound = 'Not Found';
    }

    /**
     * Inserts new node with value into BST
     * 
     * @param {Number} value value of node
     * @returns BST instance
     */
    insert(value) {
        // create new node
        const node = new Node(value);
        // if root is empty, it is root node:
        if (this.root === null) {
            this.root = node;
            return this;
        }

        let current = this.root;

        while (current) {
            if (value > current.value) {
                if (current.right) {
                    current = current.right;
                } else {
                    current.right = node;
                    break;
                }
            } else {
                if (current.left) {
                    current = current.left;
                } else {
                    current.left = node;
                    break;
                }
            }
        }
        return this;
    }

    /**
     * Looks up for the value
     * 
     * @param {Number} value valune to find
     * @returns {Object} node containing searching value
     */
    lookup(value) {
        if (!this.root) {
            return this.notFound;
        }

        let node = this.root;

        while (node.value !== value) {  // worst-case scenario -> O(log n)
            if (value > node.value) {
                if (!node.right) {
                    return this.notFound;
                }
                node = node.right;
            } else {
                if (!node.left) {
                    return this.notFound;
                }
                node = node.left;
            }
        }

        return node;
    }

    // remove
}

const tree = new BinarySearchTree();
tree.insert(9);
tree.insert(4);
tree.insert(6);
tree.insert(20);
tree.insert(170);
tree.insert(15);
tree.insert(1);

console.log(JSON.stringify(traverse(tree.root)));

//     9
//  4     20
//1  6  15  170

console.log(tree.lookup(4));
console.log(tree.lookup(22)); // Not Found
console.log(tree.lookup(9));
console.log(tree.lookup(8)); // Not Found
console.log(tree.lookup(15));
console.log(tree.lookup(9));
