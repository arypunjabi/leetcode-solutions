class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sortedNums = sorted(nums)
        res = set()
        
        for a in range(len(nums)-2):
            b = a + 1
            c = len(nums)-1

            while b < c:
                sum3 = sortedNums[a] + sortedNums[b] + sortedNums[c]
                if sum3 == 0:
                    res.add((sortedNums[a], sortedNums[b], sortedNums[c]))
                    b += 1
                    c -= 1
                elif sum3 > 0:
                    c -= 1
                elif sum3 < 0:
                    b += 1
        return list(res)
