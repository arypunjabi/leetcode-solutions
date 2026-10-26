class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def simulate(speed):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/speed)
            return hours

        L = 1
        R = 0
        for pile in piles:
            R = max(pile, R)

        res = -1
        
        while L <= R:
            m = (L + R) // 2
            hour = simulate(m)

            if hour <= h:
                res = m
                R = m - 1
            elif hour > h:
                L = m + 1
        
        return res
                