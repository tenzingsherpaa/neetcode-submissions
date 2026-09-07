class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Given an array of strs, group all anagrams together into sublists.
        #You may return the output in any order

        #Initial thought
        #

        res = defaultdict(list)
        for s in strs:

            count = [0] * 26 #for 26 letters of the alphabet

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()