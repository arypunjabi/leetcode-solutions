class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        L = 0
        R = 0
        sum = 0
        res = len(nums) + 1

        while R < len(nums):
            sum += nums[R]
            if sum >= target:
                while sum >= target and L <= R:
                    res = min(res, R - L + 1)
                    sum -= nums[L]
                    L += 1
            R += 1
        
        return 0 if (res == len(nums) + 1) else res