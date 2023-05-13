class MinStack:

    def __init__(self):
        self.stack = []
        self._minimum = 0

    def push(self, val: int) -> None:
        if not self.stack:
            self._minimum = val
            self.stack.append(val)
        elif val < self._minimum:
            self.stack.append(val * 2 - self._minimum)
            self._minimum = val
        else:
            self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] < self._minimum:
            self._minimum = self._minimum * 2 - self.stack[-1]
        self.stack.pop()

    def top(self) -> int:
        if self.stack[-1] < self._minimum:
            return self._minimum
        return self.stack[-1]

    def getMin(self) -> int:
        return self._minimum
