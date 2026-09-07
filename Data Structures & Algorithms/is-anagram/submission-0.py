class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       #given 2 strings s and t, return true if these two are anagrams 
       #make a hash table to keep track of say s and then see if all the
       #letters in the hash table have same value

        countS, countT = {}, {}


        if len(s) != len(t):
            return False


        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
            
        return True