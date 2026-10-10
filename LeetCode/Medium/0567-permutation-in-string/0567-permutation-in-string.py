class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        dic = {}
        for c in s1:
            dic[c] = dic.get(c, 0) + 1

        target = len(dic)  # number of unique chars to match
        formed = 0         # how many chars have reached count 0
        L = 0

        for R in range(len(s2)):
            # Expand window: consume s2[R]
            if s2[R] in dic:
                dic[s2[R]] -= 1
                if dic[s2[R]] == 0:
                    formed += 1

            # Shrink window when it exceeds len(s1)
            while R - L + 1 > len(s1):
                if s2[L] in dic:
                    if dic[s2[L]] == 0:
                        formed -= 1
                    dic[s2[L]] += 1
                L += 1

            # Check if current window is a valid permutation
            if formed == target:
                return True

        return False