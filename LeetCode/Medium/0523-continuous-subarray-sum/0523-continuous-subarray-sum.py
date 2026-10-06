class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        myDict = {}
        myDict[0] = -1
        count = 0

        for i in range(len(nums)):
            count += nums[i]
            if (count % k) in myDict and myDict[count % k] != i-1:
                return True
            if (count % k) not in myDict:
                myDict[count % k] = i

        return False

