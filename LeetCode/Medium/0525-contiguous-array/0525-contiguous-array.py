class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        runningSum = 0
        dic = {}
        dic[0] = -1
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                runningSum -= 1
            else:
                runningSum += 1
            
            if runningSum in dic:
                res = max(res, i-dic[runningSum])
            else:
                dic[runningSum] = i
        
        return res
