class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # DP
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        l1,l2 = len(word1),len(word2)
        dp = [[-1 for _ in range(l2)] for _ in range(l1)]
        for i in range(l1):
            for j in range(l2):
                if i == 0 and j == 0:
                    if word1[i] == word2[j]:
                        dp[0][0] = 0
                    else:
                        dp[0][0] = 1
                    continue
                if i == 0:
                    if word1[i] == word2[j] and dp[0][j-1] > j-1:
                        dp[0][j] = dp[0][j-1]
                    else:
                        dp[0][j] = dp[0][j-1] + 1 # insert char
                    continue
                if j == 0:
                    if word1[i] == word2[j] and dp[i-1][0] > i-1:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] + 1 # ins
                    continue
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
        
        return dp[-1][-1]
                
                