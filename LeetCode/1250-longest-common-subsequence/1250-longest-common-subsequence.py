class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 2-dim DP
        l1,l2 = len(text1),len(text2)
        dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]
        for idx1 in range(1,l1+1):
            for idx2 in range(1,l2+1):
                if text1[idx1-1] == text2[idx2-1]:
                    dp[idx1][idx2] = dp[idx1-1][idx2-1] + 1
                else:
                    dp[idx1][idx2] = max(dp[idx1-1][idx2],dp[idx1][idx2-1])
        return dp[l1][l2]