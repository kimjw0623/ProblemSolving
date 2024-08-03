class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        target = -1
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                target = i-1
                break
        if target == -1:
            nums.reverse()
            return
        first_item = -1
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[target]:
                first_item = i
                break
        
        nums[first_item],nums[target] = nums[target],nums[first_item]
        nums[:] = nums[:target+1]+nums[target+1:][::-1]
        return