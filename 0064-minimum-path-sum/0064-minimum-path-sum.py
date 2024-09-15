from collections import deque
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # (m+n)!/m!*n!
        # que = deque()
        # h,w = len(grid),len(grid[0])
        # visited = [[False for _ in range(w)] for _ in range(h)]
        # mv = [(1,0),(0,1)]
        # que.append([0,0,grid[0][0]])
        # ans_list = []
        # while que:
        #     cur = que.popleft()
        #     if cur[1] == h-1 and cur[0] == w-1:
        #         ans_list.append(cur[2])
        #     for mx,my in mv:
        #         nx = mx+cur[0]
        #         ny = my+cur[1]
        #         if nx < w and ny < h:
        #             que.append([nx,ny,cur[2]+grid[ny][nx]])
        
        # return min(ans_list)

        h,w = len(grid),len(grid[0])
        dp = [[-1 for _ in range(w)] for _ in range(h)]

        dp[0][0] = grid[0][0]
        for x in range(1,w):
            dp[0][x] = dp[0][x-1] + grid[0][x]
        for y in range(1,h):
            dp[y][0] = dp[y-1][0] + grid[y][0]

        for y in range(1,h):
            for x in range(1,w):
                dp[y][x] = min(dp[y-1][x],dp[y][x-1])+grid[y][x]
        
        return dp[-1][-1]
