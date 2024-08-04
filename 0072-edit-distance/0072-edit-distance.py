class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1,l2 = len(word1),len(word2)
        dp = [0 for _ in range(l2+1)]
        temp = [0 for _ in range(l2+1)]
        for i in range(l2+1):
            dp[i] = i

        for i in range(1,l1+1):
            dp[0] = i
            temp[0] = i-1
            for j in range(1,l2+1):
                temp[j] = dp[j]
                if word1[i-1] == word2[j-1]:
                    dp[j] = temp[j-1]
                else:
                    dp[j] = min(temp[j-1],dp[j-1],dp[j]) + 1
            
            print(dp,temp)
        return dp[-1]
                

