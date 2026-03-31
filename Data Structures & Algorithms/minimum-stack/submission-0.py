class MinStack:

    def __init__(self):
        self.stack = []
        self.key = 0
        self.mini = {}

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.key == 0:
            self.mini[self.key] = val
        else:
            self.mini[self.key] = min(self.mini[self.key-1], val)
        self.key+=1
        
        
    def pop(self) -> None:
        self.stack.pop()
        if self.key != 0:
            self.key -=1
        else:
            self.mini[self.key] = None
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.mini[self.key - 1] if self.key != 0 else self.mini[self.key]

        
