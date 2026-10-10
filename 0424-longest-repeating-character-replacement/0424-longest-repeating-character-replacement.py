class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        L = 0
        mostCommonChar = s[0]
        dic[mostCommonChar] = 1
        res = 1

        for R in range(1, len(s)):
            dic[s[R]] = dic.get(s[R], 0) + 1
            if dic[s[R]] > dic[mostCommonChar]:
                mostCommonChar = s[R]
            if (dic[mostCommonChar] + k) < (R - L + 1):
                dic[s[L]] -= 1
                L += 1
            res = R - L + 1
        
        return res