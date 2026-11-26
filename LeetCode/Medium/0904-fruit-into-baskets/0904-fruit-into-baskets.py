class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        """L = 0
        fruitSet = set()
        temp = -1
        res = 0

        for R in range(len(fruits)):
            if fruits[R] not in fruitSet:
                if len(fruitSet) < 2:
                    set.fruitSet(fruits[R])
                else:"""
        deq = deque()
        L = 0
        res = 0

        for R in range(len(fruits)):
            if not deq or (len(deq) < 2 and fruits[R] != deq[-1][0]):
                deq.append([fruits[R], R])
            elif fruits[R] == deq[-1][0]:
                deq[-1][1] = R
            elif fruits[R] == deq[0][0]:
                deq.popleft()
                deq.append([fruits[R], R])
            else:
                L = deq[0][1] + 1
                deq.popleft()
                deq.append([fruits[R], R])
            res = max(res, R-L+1)
        return res
            






                    
