class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        h,w = len(matrix),len(matrix[0])
        max_length = 0
        for i in range(h):
            for j in range(w):
                value_list = []
                if i-1 < 0 or i > h-1 or j-1 < 0 or j > w-1:
                    matrix[i][j] = int(matrix[i][j])
                elif int(matrix[i][j])==1:
                    matrix[i][j] = min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1]) + 1
                else: # matrix is List[List[str]], convert to int
                    matrix[i][j] = int(matrix[i][j])
                max_length = max(max_length,matrix[i][j])

        return max_length*max_length
