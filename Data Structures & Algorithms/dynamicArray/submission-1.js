class DynamicArray {
    /**
     * @constructor
     * @param {number} capacity
     */
    constructor(capacity) {
        this.dArray = {}
        this.nextIndexToInsert = 0
        this.capacity = capacity
        for(let i = 0; i < capacity; i++){
            this.dArray[i] = null
        }
    }

    /**
     * @param {number} i
     * @returns {number}
     */
    get(i) {
        return this.dArray[i]
    }

    /**
     * @param {number} i
     * @param {number} n
     * @returns {void}
     */
    set(i, n) {
        this.dArray[i] = n
        if(this.nextIndexToInsert === i) {
             this.nextIndexToInsert = i + 1
        } 
    }

    /**
     * @param {number} n
     * @returns {void}
     */
    pushback(n) {
        if(this.nextIndexToInsert >= this.capacity){
            this.resize()
            this.set(this.nextIndexToInsert, n)
        }else this.set(this.nextIndexToInsert, n)
    }

    /**
     * @returns {number}
     */
    popback() {
        const index = this.nextIndexToInsert - 1
        this.nextIndexToInsert = index
        return this.get(index)
    }

    /**
     * @returns {void}
     */
    resize() {
        for(let i = this.capacity - 1 ; i > this.capacity * 2; i++){
            this.dArray[i] = null
        }
        this.capacity = this.capacity * 2
    }

    /**
     * @returns {number}
     */
    getSize() {
        return this.nextIndexToInsert
    }

    /**
     * @returns {number}
     */
    getCapacity() {
        return this.capacity
    }
}
