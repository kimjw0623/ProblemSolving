class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # if circular: minimum
        # if not circular: maximum
        # DP
        max_dp = [0 for _ in range(len(nums))]
        min_dp = [0 for _ in range(len(nums))]
        # Get maximum
        for i in range(len(nums)):
            if i == 0:
                max_dp[i] = nums[i]
                continue
            if max_dp[i-1] > 0:
                max_dp[i] = max_dp[i-1]+nums[i]
            else:
                max_dp[i] = nums[i]
            if min_dp[i-1] > 0:
                min_dp[i] = nums[i]
            else:
                min_dp[i] = min_dp[i-1]+nums[i]
        non_circular = max(max_dp)
        circular = sum(nums)-min(min_dp)
        return max(non_circular,circular)