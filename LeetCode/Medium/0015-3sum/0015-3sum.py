class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sortedNums = sorted(nums)
        res = []
        a = 0

        while a < len(nums) - 2:
            b = a + 1
            c = len(nums) - 1

            while b < c:
                if sortedNums[a] + sortedNums[b] + sortedNums[c] == 0:
                    res.append([sortedNums[a],sortedNums[b],sortedNums[c]])
                    b += 1
                    c -= 1
                    while b < c and sortedNums[b] == sortedNums[b - 1]:
                        b += 1
                elif sortedNums[a] + sortedNums[b] + sortedNums[c] < 0:
                    b += 1
                elif sortedNums[a] + sortedNums[b] + sortedNums[c] > 0:
                    c -= 1
            a += 1

            while a < (len(sortedNums)-2) and sortedNums[a] == sortedNums[a - 1]:
                a += 1

        return res
    
