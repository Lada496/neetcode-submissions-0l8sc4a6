class LinkNode {
    constructor(val, nextNode = null){
        this.val = val
        this.next = nextNode
    }
}

class LinkedList {
    constructor() {
        this.head = new LinkNode(-1)
        this.tail = this.head
    }

    /**
     * @param {number} index
     * @return {number}
     */
    get(index) {
        let curr = this.head.next;
        let i = 0;
        while (curr) {
            if (i === index) {
                return curr.val;
            }
            i++;
            curr = curr.next;
        }
        return -1;
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertHead(val) {
       const newNode = new LinkNode(val);
        newNode.next = this.head.next;
        this.head.next = newNode;
        if (!newNode.next) {
            // If list was empty before insertion
            this.tail = newNode;
        }
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertTail(val) {
        this.tail.next = new LinkNode(val)
        this.tail = this.tail.next
    }

    /**
     * @param {number} index
     * @return {boolean}
     */
    remove(index) {
        let i = 0;
        let curr = this.head;
        while (i < index && curr) {
            i++;
            curr = curr.next;
        }

        // Remove the node ahead of curr
        if (curr && curr.next) {
            if (curr.next === this.tail) {
                this.tail = curr;
            }
            curr.next = curr.next.next;
            return true;
        }
        return false;
    }

    /**
     * @return {number[]}
     */
    getValues() {
        const values = []
        let curr = this.head.next
        while(curr){
            values.push(curr.val)
            curr = curr.next
        }
        return values
    }
}
