class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.empty():
            return self.stack.pop(0)

    def peek(self) -> int:
        if not self.empty():
            return self.stack[0]

    def empty(self) -> bool:
        return self.stack == []
