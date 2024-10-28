
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        h,w = len(grid),len(grid[0])
        dp = [[-1 for i in range(w)] for _ in range(h)]
        old_row = [9999999 for _ in range(w)]
        
        for y in range(h):
            new_row = [0 for _ in range(w)]
            for x in range(w):
                if y == 0 and x == 0:
                    new_row[0] = grid[0][0]
                    continue
                upper_val = old_row[x]
                if x == 0:
                    left_val = 99999
                else:
                    left_val = new_row[x-1]
                print(left_val)
                new_row[x] = min(upper_val,left_val) + grid[y][x]
            old_row = new_row[:]

        return new_row[-1]