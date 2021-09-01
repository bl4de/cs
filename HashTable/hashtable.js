class HashTable {
    constructor(size) {
        this.data = new Array(size);
    }

    _hash(key) {
        let hash = 0;
        for (let i = 0; i < key.length; i++) {
            hash = (hash + key.charCodeAt(i) * i) % this.data.length
        }
        return hash;
    }

    set(key, val) {
        if (key && val) {
            let address = this._hash(key);
            if (!this.data[address]) {
                this.data[address] = [];
            } 
            this.data[address].push([key,val]);
        }
    }

    get(key) {
        let address = this._hash(key);
        const bucket = this.data[address];
        if (bucket) {
            for (let i = 0; i < bucket.length; i++) {
                if (bucket[i][0] === key) {
                    return bucket[i][1];
                }
            }
        }
        return undefined;
    }

    keys() {
        const keysArr = [];
        for (let i = 0; i < this.data.length; i++) {
            if (this.data[i]) {
                keysArr.push(this.data[i][0][0]);
            }
        }
        return keysArr;
    }
}

const myHashTable = new HashTable(50);

myHashTable.set('grapes', 10000)
myHashTable.set('apples', 9)
myHashTable.set('oranges', 2)

console.log(myHashTable.get('grapes'));
console.log(myHashTable.get('apples'));
console.log(myHashTable.get('oranges'));

console.log(myHashTable.keys());