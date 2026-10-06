class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        newList = [1] * len(nums)

        for i in range(1, len(nums)):
            newList[i] = newList[i-1] * nums[i-1]
        postFix = 1
        for i in range(len(nums) - 1, -1, -1):
            temp = nums[i]
            nums[i] = postFix * newList[i]
            postFix *= temp
        
        return nums