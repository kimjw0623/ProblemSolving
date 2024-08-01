class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp
        ans = []
        # def recursive(cur_val,idx):
        #     if idx==len(nums):
        #         if cur_val == target:
        #             ans.append("1")
        #         return
        #     for i in [-1,1]:
        #         recursive(cur_val+i*nums[idx],idx+1)
        # recursive(0,0)

        # visited: same idx, 
        mapping = dict()
        mapping[0] = 1
        for i in range(len(nums)):
            new_mapping = dict()
            for key in mapping.keys():
                if key-nums[i] not in new_mapping: new_mapping[key-nums[i]] = 0
                if key+nums[i] not in new_mapping: new_mapping[key+nums[i]] = 0
                new_mapping[key-nums[i]] += mapping[key]
                new_mapping[key+nums[i]] += mapping[key]
            mapping = new_mapping
        return mapping.get(target,0)