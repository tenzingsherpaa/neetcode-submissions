class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = dict()
        countT = dict()
        for l in s:
            if l in countS:
                num = countS.get(l)
                countS[l] = num + 1
            else:
                countS[l] = 1
        for l in t:
            if l in countT:
                num = countT.get(l)
                countT[l] = num + 1
            else:
                countT[l] = 1

        return countS == countT


        