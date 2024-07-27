class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # stack with no order... (not monotonic stack!!)
        # [4 3 6] [4 5 6], 
        ans = []
        stack = []
        elem_to_max = dict()
        for item in nums2[::-1]:
            if not stack:
                stack.append(item)
                elem_to_max[item] = -1
            else:
                while stack and item > stack[-1]:
                    stack.pop()
                if stack:
                    elem_to_max[item] = stack[-1]
                else:
                    elem_to_max[item] = -1
                stack.append(item)
        for item in nums1:
            ans.append(elem_to_max[item])
        return ans