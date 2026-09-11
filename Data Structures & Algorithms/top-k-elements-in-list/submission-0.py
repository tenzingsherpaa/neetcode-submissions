class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Given an integer array nums[] and an integer k, return the k most frequent elements within the array

        # Ex 1: Input nums = [1,2,2,3,3,3] Output = Answer [2,3]

        numTops = {}
        for num in nums:
            if num not in numTops:
                numTops[num] = 1
            else:
                numTops[num] = numTops.get(num, 0) + 1

        sorted_Values = sorted(numTops.items(),key=lambda x:x[1],  reverse=True)

        topKth = [pair[0] for pair in sorted_Values[:k]]

        return topKth