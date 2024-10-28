class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        # nums = list(set(nums))
        num_set = set(nums)
        ans = 0
        for num in num_set:
            if num+1 in num_set:
                continue
            cnt = 1
            target = num-1
            while target in num_set:
                target -= 1
                cnt += 1
            ans = max(ans,cnt)
        return ans