class MinHeap {
    constructor() {
        this.heap = [];
    }

    size() {
        return this.heap.length;
    }

    peek() {
        return this.heap[0];
    }

    push(value) {
        this.heap.push(value);

        let cur = this.heap.length - 1;

        while (cur > 0) {
            let parent = Math.floor((cur - 1) / 2);

            if (this.heap[parent] <= this.heap[cur]){
                break;
            }

            [this.heap[parent], this.heap[cur]] = [this.heap[cur], this.heap[parent]];
            cur = parent;
        }
    }

    pop() {
        if (this.heap.length === 0) return null;
        if (this.heap.length === 1) return this.heap.pop();

        const root = this.heap[0];
        this.heap[0] = this.heap.pop();

        let cur = 0;

        while (true) {
            let left = cur * 2 + 1;
            let right = cur * 2 + 2;
            let smallest = cur;

            if (left < this.heap.length && this.heap[left] < this.heap[smallest]) {
                smallest = left;
            }

            if (right < this.heap.length && this.heap[right] < this.heap[smallest]) {
                smallest = right;
            }

            if (smallest === cur){
                break;
            }
            [this.heap[cur], this.heap[smallest]] = [this.heap[smallest], this.heap[cur]];

            cur = smallest;
        }

        return root;
    }
}