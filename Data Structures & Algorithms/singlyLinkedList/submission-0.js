class ListNode {
    constructor(value){
        this.next = null;
        this.value = value;
    }
}

class LinkedList {
    constructor() {
        this.head = new ListNode(-1); // Dummy head node
        this.tail = this.head;
    }

    /**
     * @param {number} index
     * @return {number}
     */
    get(index) {
        let i = 0;
        let curr = this.head.next; // Start from the first actual node
        while (i < index && curr != null) {
            i++;
            curr = curr.next;
        }
        return curr == null ? -1 : curr.value;
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertHead(val) {
        let newNode = new ListNode(val);
        newNode.next = this.head.next;
        this.head.next = newNode;
        if (this.tail === this.head) { // If the list was empty
            this.tail = newNode;
        }
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertTail(val) {
        this.tail.next = new ListNode(val);
        this.tail = this.tail.next;
    }

    /**
     * @param {number} index
     * @return {boolean}
     */
    remove(index) {
        let i = 0;
        let curr = this.head;
        while (i < index && curr.next != null) {
            i++;
            curr = curr.next;
        }

        if (curr.next != null) {
            if (curr.next == this.tail) {
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
        let values = [];
        let curr = this.head.next; // Start from the first actual node
        while (curr != null) {
            values.push(curr.value);
            curr = curr.next;
        }
        return values;
    }
}
