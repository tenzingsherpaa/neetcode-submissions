'''''
Create decision trees to visualize and solve it better 

Recursive Brute Force Solution will have O(2^n), however since there are a lot of repeated work there can be improvements

Dynamic Programming Solution (DP):
Use the given array to iterate backwards and find out what the cost from each position is to get to the top



'''''




class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])

        return min(cost[0], cost[1])