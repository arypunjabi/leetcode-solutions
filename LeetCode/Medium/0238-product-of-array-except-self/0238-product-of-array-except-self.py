class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixArray = [1] * len(nums)
        for i in range(1, len(nums)):
            prefixArray[i] = prefixArray[i-1] * nums[i-1]
        
        postFix = 1
        for i in range(len(nums) - 1, -1, -1):
            prefixArray[i] = prefixArray[i] * postFix
            postFix *= nums[i]
        
        return prefixArray
