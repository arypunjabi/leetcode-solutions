class StockSpanner:
    def __init__(self):
        self.stockList = deque()

    def next(self, price: int) -> int:
        runningTotal = 0

        while self.stockList and self.stockList[-1][0] <= price:
            runningTotal += self.stockList.pop()[1]
        self.stockList.append((price, runningTotal + 1))

        return runningTotal + 1