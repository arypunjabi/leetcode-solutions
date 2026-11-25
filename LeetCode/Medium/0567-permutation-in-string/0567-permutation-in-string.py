class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Dic = {}
        s2Dic = {}

        for c in s1:
            s1Dic[c] = s1Dic.get(c, 0) + 1
        
        R = 0
        L = 0
        while R < len(s2):
            s2Dic[s2[R]] = s2Dic.get(s2[R], 0) + 1
            if s2[R] not in s1Dic:
                s2Dic = {}
                L = R + 1
            else:
                while s2Dic[s2[R]] > s1Dic[s2[R]]:
                    s2Dic[s2[L]] -= 1
                    L += 1
            if s2Dic == s1Dic:
                return True
            R += 1

        return False
