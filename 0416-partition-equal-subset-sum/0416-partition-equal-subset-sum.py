class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # sorting first
        # make sum(nums)//2
        
        # if sum(nums) % 2 == 1:
        #     return False
        # half = sum(nums) // 2
        # @cache
        # def rec(s,i):
        #     if i > len(nums)-1 or s < 1:
        #         return False
        #     if s == nums[i]:
        #         return True
        #     return rec(s,i+1) or rec(s-nums[i],i+1)
        # return rec(half,0)
        total_sum = sum(nums)
        if total_sum & 1: return False
        half = total_sum // 2
        dp = [True] + [False]*half
        for num in nums:
            for j in range(half, 0,-1):
                if j-num >= 0 and dp[j-num]: dp[j] = True
        return dp[half] 
        