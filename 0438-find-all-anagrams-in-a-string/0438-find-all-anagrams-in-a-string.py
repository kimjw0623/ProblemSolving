from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target_counter = Counter(p)
        new_counter = Counter()
        length = len(p)

        def isSame(target,new):
            is_same = True
            for k in target.keys():
                if target[k] != new[k]:
                    is_same = False
                    break
            return is_same

        ans = []
        for idx,char in enumerate(s):
            new_counter[char] += 1
            if new_counter[char] == 0:
                del new_counter[char]
            
            if idx >= length:
                new_counter[s[idx-length]] -= 1
                if new_counter[s[idx-length]] == 0:
                    del new_counter[s[idx-length]]

            if isSame(target_counter,new_counter):
                ans.append(idx-length+1)

        return ans
