class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # target_sum 을 만족하는 set이 존재해야 함
        # brute force: X
        # DP? target_sum 을 만족하는 범위가 적으므로 가능할 듯
        if sum(nums)%2: return False
        target_sum = sum(nums)//2

        sum_dict = {}
        for num in nums:
            if not sum_dict:
                sum_dict[num] = True
                continue
            for s in list(sum_dict.keys())[:]:
                sum_dict[s+num] = True
            sum_dict[num] = True
        print(sum_dict)
        return sum_dict.get(target_sum,False) 