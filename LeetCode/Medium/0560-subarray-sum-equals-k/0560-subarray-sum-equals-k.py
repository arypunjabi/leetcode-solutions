class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {}
        dic[0] = 1
        count = 0
        res = 0

        for i in range(len(nums)):
            count += nums[i]
            if (count - k) in dic:
                res += dic[count - k]
            
            dic[count] = dic.get((count), 0) + 1
        
        return res