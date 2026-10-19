class Solution:
    def maxArea(self, height: list[int]) -> int:
        L = 0
        R = len(height) - 1
        res = 0

        while L < R:
            vol = (R - L) * min(height[L], height[R])
            res = max(res, vol)

            if height[L] < height[R]:
                L += 1
            else:
                R -= 1

        return res