from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target_counter = Counter(p)
        ans = []
        left = 0
        for idx,char in enumerate(s):
            target_counter[char] -= 1
            while target_counter[char] < 0:
                target_counter[s[left]] += 1
                left += 1
            if idx-left+1 == len(p):
                ans.append(left)

        return ans
