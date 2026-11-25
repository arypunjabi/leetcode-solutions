class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        remainders = {}
        runningSum = 0

        for i in range(len(nums)):
            runningSum += nums[i]

            if runningSum % k == 0 and i > 0:
                return True

            if (runningSum % k) in remainders and remainders[runningSum % k] < (i - 1):
                return True
            if (runningSum % k) not in remainders:
                remainders[runningSum % k] = i
        
        return False