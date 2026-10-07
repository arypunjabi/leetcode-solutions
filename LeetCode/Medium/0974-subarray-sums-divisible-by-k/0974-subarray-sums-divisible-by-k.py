class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        dic = {}
        dic[0] = 1
        count = 0
        res = 0

        for i in range(len(nums)):
            count += nums[i]
            if (count % k) in dic:
                res += dic[count % k]
                dic[count % k] += 1
            else:
                dic[count % k] = 1

        return res
            