class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Greater than neighbor
        l,r = 0,len(nums)-1
        while l < r:
            mid = (l+r)//2
            # if r==0 or l==len(nums)-1: return r
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid+1
        
        return l