class Solution:
    # Return a list of list of strings
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        gAnagrams = defaultdict(list)
        #Edge cases for other examples
        if len(strs) == 0: return {{}}
        #elif len(strs) == 1: return strs

        for s in strs:
            sortedS = ''.join(sorted(s))
            gAnagrams[sortedS].append(s)
        
        return list(gAnagrams.values())




    

   