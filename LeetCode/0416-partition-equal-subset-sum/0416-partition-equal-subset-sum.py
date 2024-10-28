class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 0/1 knapsack problem
        if sum(nums)%2: return False
        target_sum = sum(nums)//2
        # recursive
        @cache
        def recursive(target,idx):
            if target == 0:
                return True
            if idx >= len(nums) or target < 0:
                return False
            return recursive(target-nums[idx],idx+1) or recursive(target,idx+1)
        return recursive(target_sum,0)
