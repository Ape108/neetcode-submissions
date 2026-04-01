class MinStack:

    def __init__(self):
        self.array = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.array.append(val)
        if not self.minStack or val < self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])
        
    def pop(self) -> None:
        self.array.pop(-1)
        self.minStack.pop(-1)


    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
