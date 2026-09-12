class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Given an array of integers [numbers] that is sorted in non-decreasing order

        # First thought is that a naive two pointer technique could compute the elements
        # Iterate through the array with two pointers, l in the start and r in the end. 
        # Keep doing it until the target is reached
        #Return a List[two index]

        l, r = 0, len(numbers) - 1
        while l < r and l != r:
            
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            
            elif numbers[l] + numbers[r] > target:
                r -= 1

            elif numbers[l] + numbers[r] < target:
                l += 1
            
            


        return []




    