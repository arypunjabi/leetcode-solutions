class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        sums = {}
        count = 0
        sums[0] = 1
        res = 0

        for num in nums:
            count += num
            rem = count % k

            res += sums.get(rem, 0)
            sums[rem] = 1 + sums.get(rem, 0)
        
        return res