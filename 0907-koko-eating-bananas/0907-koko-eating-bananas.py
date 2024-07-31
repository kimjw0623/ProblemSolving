class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        def get_hours(k):
            cur_sum = 0
            for pile in piles:
                cur_sum += pile//k
                if pile%k: cur_sum += 1
            return cur_sum

        l,r = 1,max(piles)
        while l<r:
            mid = (l+r)//2
            if get_hours(mid) > h:
                l = mid+1
            else:
                r = mid

        return l