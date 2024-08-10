class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 1 3 5 7 4 2 4
        cur_sum = 0
        sum_dict = dict()
        sum_dict[0] = 1
        ans = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            ans += sum_dict.get(cur_sum-k,0)
            sum_dict[cur_sum] = sum_dict.get(cur_sum,0) + 1

        return ans