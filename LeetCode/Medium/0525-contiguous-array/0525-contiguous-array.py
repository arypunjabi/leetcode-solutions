class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {}
        count = 0
        res = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            
            if count == 0:
                res = i + 1
            
            if count in dic:
                res = max(res, i - dic[count])
            else:
                dic[count] = i
        
        return res

