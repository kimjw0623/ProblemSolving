class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # ABAAABBBB
        if len(s) <= k: return len(s)
        # 같은 문자의 위치만 중요
        # sliding window의 size가 바뀔 수도 (l,r을 통해 구현)
        freq_dict = {}
        l,r = 0,0
        max_seq_len = 0
        for r,char in enumerate(s):
            if char not in freq_dict:
                freq_dict[char] = 1
            else:
                freq_dict[char] += 1
            max_freq = max(freq_dict.values())

            if max_freq + k < r-l+1:
                freq_dict[s[l]] -= 1
                if freq_dict[s[l]] == 0:
                    del freq_dict[s[l]]
                l += 1
            else:
                max_seq_len = max(max_seq_len,r-l+1)
        return max_seq_len