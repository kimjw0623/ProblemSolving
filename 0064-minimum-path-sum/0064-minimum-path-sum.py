
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        h,w = len(grid),len(grid[0])
        dp = [[-1 for i in range(w)] for _ in range(h)]
        
        for y in range(h):
            for x in range(w):
                if y == 0 and x == 0: 
                    dp[0][0] = grid[0][0]
                    continue
                upper_val = 9999999
                left_val = 9999999
                if y != 0:
                    upper_val = dp[y-1][x]
                if x != 0:
                    left_val = dp[y][x-1]
                dp[y][x] = min(upper_val,left_val) + grid[y][x]
        print(dp[-1])
        return dp[-1][-1]
