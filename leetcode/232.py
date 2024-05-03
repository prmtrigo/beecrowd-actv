class MyQueue:

    def __init__(self):
        self.primeira_estaca = []
        self.segunda_estaca = []
        #funciona tipo o deque no 225.py

    def push(self, x: int) -> None:
        self.primeira_estaca.append(x)
        #append pop left()

    def pop(self) -> int:
        if not self.segunda_estaca:

            while self.primeira_estaca:
                self.segunda_estaca.append(self.primeira_estaca.pop())
        return self.segunda_estaca.pop()

    def peek(self) -> int:
        if not self.segunda_estaca:

            while self.primeira_estaca:
                self.segunda_estaca.append(self.primeira_estaca.pop())
        return self.segunda_estaca[-1]

    def empty(self) -> bool:
        return not self.primeira_estaca and not self.segunda_estaca