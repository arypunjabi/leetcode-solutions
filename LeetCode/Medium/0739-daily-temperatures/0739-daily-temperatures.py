class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        monoStack = deque()

        for i in range(len(temperatures)):
            while monoStack and monoStack[-1][0] < temperatures[i]:
                diff = monoStack.pop()[1]
                res[diff] = i-diff
            monoStack.append((temperatures[i], i))
        
        return res