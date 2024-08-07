class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_palindrome(s):
            is_valid = True
            for i in range(len(s)):
                if s[i]!=s[len(s)-i-1]:
                    is_valid = False
            return is_valid

        dp = [[] for _ in range(len(s))]
        dp[0] = [[s[0]]]
        for i in range(1, len(s)):
            for idx in range(i+1):
                if is_palindrome(s[idx:i+1]):
                    if idx == 0:
                        dp[i].append([s[idx:i+1]])
                    else:
                        for cand in dp[idx-1]:
                            dp[i].append(cand+[s[idx:i+1]])
        return dp[-1]