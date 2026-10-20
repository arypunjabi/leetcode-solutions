class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monoStack = []
        res = [0] * len(temperatures)
        monoStack.append((0, temperatures[0]))
        for i in range(1, len(temperatures)):
            while monoStack and temperatures[i] > monoStack[-1][1]:
                res[monoStack[-1][0]] = (i - monoStack[-1][0])
                monoStack.pop()
            monoStack.append((i, temperatures[i]))
        return res