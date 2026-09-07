'''''
# Some intial Thoughts
# Create a hashmap to store the permuatation of 1 and 2 that add to n so those aren't repeated
# See if the two loop adds to the n between 1 and 2
# Questions: What is the highest n? What to do with 0 case? 

Neetcode:
Decision Trees:
we can do two decisions either 1 or 2
when n = 3
        0
    1       2
  2  3    3   4
3  4

DFS on a Decision tree (2^n)

But we can improve the time with

caching the trees for 2 as it is the same on right 

Solution would be O(n) when you store the tress that are solved already
aka memoization

Think bottom up approach
Store how many different ways it takes to get to n in an array
        0  1  2  3
DP =   [{3  {2  {1}  1}}]


'''''



class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one


