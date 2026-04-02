class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        minimum = min(self.minstack[-1] if len(self.minstack) > 0 else val, val)
        self.minstack.append(minimum)
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
