class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sFreq = {}
        L = 0
        maxLen = 0
        currLen = 0

        for R in range(len(s)):
            if s[R] in sFreq:
                sFreq[s[R]] += 1
            else:
                sFreq[s[R]] = 1
            
            currLen += 1
            
            while sFreq[s[R]] > 1:
                sFreq[s[L]] -= 1
                L += 1
                currLen -= 1
            
            maxLen = max(currLen, maxLen)

        return maxLen
        