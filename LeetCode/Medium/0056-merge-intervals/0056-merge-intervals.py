class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x : x[0])
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            temp = intervals[i]
            if temp[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], temp[1])
            else:
                res.append(temp)
        
        return res