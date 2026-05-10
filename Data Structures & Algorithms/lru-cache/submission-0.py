class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
class LRUCache:


    def __init__(self, capacity: int):
        self.cache = {} # key: node
        self.cap = capacity
        self.left = self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def insert(self, node):
        prev = self.right.prev
        next = self.right
        prev.next = node
        node.prev = prev
        node.next = next
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key,value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
