class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s
        ans = ""
        max_len = 0
        for i in range(len(s)):
            for j in range(i+1):
                if i+j < len(s):
                    if s[i-j] != s[i+j]:
                        break
                    else:
                        if max_len < 2*j+1:
                            max_len = 2*j+1
                            ans = s[i-j:i+j+1]
            for j in range(i+1):
                if i+j+1 < len(s):
                    if s[i-j] != s[i+j+1]:
                        break
                    else:
                        if max_len < 2*j+2:
                            max_len = 2*j+2
                            ans = s[i-j:i+j+2]
        # print(max_len)
        return ans