class Node:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class Deque:
    
    def __init__(self):
        self.head = self.tail = None

    def isEmpty(self) -> bool:
            return not bool(self.head) # return true when bool(self.head), else false
        

    def append(self, value: int) -> None:
        node = Node(value)
        if self.isEmpty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def appendleft(self, value: int) -> None:
        node = Node(value)
        if self.isEmpty():
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
  

# 1 -> 2 -> 3
# 2 -> 3
    def pop(self) -> int:
        if self.isEmpty():
            return -1
        elif self.head == self.tail:
            val = self.head.val
            self.head = self.tail = None
            return val
        else:
            head = self.head # 1
            self.head.next.prev = None
            self.head = self.head.next #2
            return head.val

# 1 -> 2 -> 3
# 1 -> 2
    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        elif self.head == self.tail:
            val = self.head.val
            self.head = self.tail = None
            return val
        else:
            tail = self.tail # 3
            self.tail.prev.next = None
            self.tail = self.tail.prev
            return tail.val
        
