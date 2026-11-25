class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        L = 0
        res = len(nums) + 1
        runningSum = 0

        for R in range(len(nums)):
            runningSum += nums[R]
            while runningSum >= target:
                res = min(res, R-L+1)
                runningSum -= nums[L]
                L += 1

        if res == len(nums) + 1:
            return 0
        else:
            return res