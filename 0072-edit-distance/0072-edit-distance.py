class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # horse -> rorse -> rose -> ros
        # max candidnate: max(len(word1),len(word2))
        # candy dye -> 4
        
        l1,l2 = len(word1),len(word2)
        dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]
        for i in range(l2+1):
            dp[0][i] = i
        for i in range(l1+1):
            dp[i][0] = i
        # dp[m,n] -> word1[:m], word2[:n] case
        # hors -> ros: 2, horse -> ro: 4
        # hor -> ro: 2
        #   r o s
        # h 1 2 3
        # o 2 1 2
        # r 2 2 2
        # s 3 3 2 
        # e 4 4 3
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j]) + 1
                    
        return dp[-1][-1]
                

