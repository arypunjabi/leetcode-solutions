class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        maxFreq = 0   # integer, never decreases
        L = 0

        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0) + 1
            maxFreq = max(maxFreq, count[s[R]])

            # shrink only while the CURRENT window is invalid
            while (R - L + 1) - maxFreq > k:
                count[s[L]] -= 1
                L += 1

            res = max(res, R - L + 1)

        return res