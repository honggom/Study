class MyStack:

    def __init__(self):
        self.stack = []
        self.count = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.count += 1

    def pop(self) -> int:
        if self.empty():
            return
        tmp = self.stack[-1]
        del self.stack[-1]
        self.count -= 1
        return tmp

    def top(self) -> int:
        if self.empty():
            return
        return self.stack[-1]

    def empty(self) -> bool:
        return self.count == 0
