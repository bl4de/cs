/**
 * Simple implementation of undirected, unweighted graph
 * using Adjacent List
 */

class Graph {

    constructor() {
        this.numberOfNodes = 0;
        this.adjacentList = {
        };
    }

    /**
     * Adds new nod eto the graph
     * 
     * @param {Object} node new graph node
     */
    addVertex(node) {
        if (node) {
            this.adjacentList[node] = [];
            this.numberOfNodes++;
        }
    }

    /**
     * Creates bidirectional linkage between nodes
     * @param {Number} node1 node 1
     * @param {Number} node2 node 2
     */
    addEdge(node1, node2) {
        for (let node in this.adjacentList) {
            if (node == node1) {
                this.adjacentList[node].push(node2);
            }
            if (node == node2) {
                this.adjacentList[node].push(node1);
            }
        }
    }

    showConnections() {
        const allNodes = Object.keys(this.adjacentList);
        for (let node of allNodes) {
            let nodeConnections = this.adjacentList[node];
            let connections = "";
            let vertex;
            for (vertex of nodeConnections) {
                connections += vertex + " ";
            }
            console.log(node + "-->" + connections);
        }
    }
}

const myGraph = new Graph();
myGraph.addVertex('0');
myGraph.addVertex('1');
myGraph.addVertex('2');
myGraph.addVertex('3');
myGraph.addVertex('4');
myGraph.addVertex('5');
myGraph.addVertex('6');
myGraph.addEdge('3', '1');
myGraph.addEdge('3', '4');
myGraph.addEdge('4', '2');
myGraph.addEdge('4', '5');
myGraph.addEdge('1', '2');
myGraph.addEdge('1', '0');
myGraph.addEdge('0', '2');
myGraph.addEdge('6', '5');

myGraph.showConnections();
//Answer:
// 0-->1 2 
// 1-->3 2 0 
// 2-->4 1 0 
// 3-->1 4 
// 4-->3 2 5 
// 5-->4 6 
// 6-->5