class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows, col = len(grid), len(grid[0])

        def dfs(grid, r, c, visit):
            if (min(r, c) < 0  or (r, c) in visit or
            r == rows or c == col or grid[r][c] == 1):
                return 0
            if r == rows - 1 and c == col - 1:
                return 1
            visit.add((r, c))
        
            #Starting Recursive Calls
            count = 0
            count += dfs(grid, r + 1, c, visit)
            count += dfs(grid, r - 1, c, visit)
            count += dfs(grid, r, c + 1, visit)
            count += dfs(grid, r, c - 1, visit)
            visit.remove((r, c))
            return count
      
        return dfs(grid, 0, 0, set())