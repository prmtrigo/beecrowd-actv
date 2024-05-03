class MyStack:

    def __init__(self):
        self.fileira = deque()

    def push(self, x: int) -> None:
        self.fileira.append(x)
        
        for i in range(len(self.fileira)-1):
            self.fileira.append(self.fileira.popleft())

    def pop(self) -> int:
        return self.fileira.popleft()

    def top(self) -> int:
        return self.fileira[0]

    def empty(self) -> bool:
        return len(self.fileira) == 0