'''
994. Rotting Oranges

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if rows == 0:
            return -1
        
        cols = len(grid[0])
        
        rotten = deque()
        fresh_cnt = 0
        
        # iterate through the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                elif grid[r][c] == 1:
                    fresh_cnt += 1
                    
        mins_passed = 0
        while rotten and fresh_cnt > 0:
            mins_passed += 1
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    xx, yy = x+dx, y + dy
                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
                        continue
                        
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue
                        
                    if grid[xx][yy] == 1:
                        grid[xx][yy] = 2
                        
                    fresh_cnt -= 1
                        
                    rotten.append((xx, yy))
                    
        return mins_passed if fresh_cnt == 0 else -1
                        
                    
        
        
                        
        