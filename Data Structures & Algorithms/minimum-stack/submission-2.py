class MinStack:
    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if (not self.stack):
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    # [5, 7, 3] - > [0, ] min = 5
    # [0, 2], min = 5
    # [0, 2, -2], min = 3

    def pop(self) -> None:
        pop = self.stack.pop()
        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        top = self.stack[-1]
        if (top < 0):
            return self.min
        return top + self.min

    def getMin(self) -> int:
        return self.min