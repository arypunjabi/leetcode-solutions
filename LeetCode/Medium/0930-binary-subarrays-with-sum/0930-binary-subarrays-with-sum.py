class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        runningSum = 0
        dic = {}
        dic[0] = [-1]
        res = 0

        for i in range(len(nums)):
            runningSum += nums[i]
            if (runningSum - goal) in dic:
                res += len(dic[runningSum - goal])
            
            if runningSum in dic:
                dic[runningSum].append(i)
            else:
                dic[runningSum] = [i]
                
        return res