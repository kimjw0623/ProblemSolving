class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        visited = [[False for _ in range(n)] for _ in range(n)]
        ans = []
        def recursive(cur_visited, cur_n, cur_ans):
            if cur_n == n: 
                ans.append(cur_ans)
                return
            for i in range(0,n):
                if cur_visited[cur_n][i]: 
                    continue
                new_visited = [arr[:] for arr in cur_visited]
                for y in range(1,n):
                    for k in [i-y,i,i+y]:
                        if k > -1 and k < n and cur_n+y < n:
                            new_visited[cur_n+y][k] = True
                recursive(new_visited,cur_n+1,cur_ans+[i])
                
        recursive(visited,0,[])

        result = []
        for arr in ans:
            cur_result = []
            for pos in arr:
                cur_result.append("."*pos+"Q"+"."*(n-pos-1))
            result.append(cur_result)
        return result