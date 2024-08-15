class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def get_num(num) -> int:
            total = mid//a + mid//b + mid//c - mid//ab - mid//ac - mid//bc + mid//abc
            return total

        ab = a * b // math.gcd(a, b)
        ac = a * c // math.gcd(a, c)
        bc = b * c // math.gcd(b, c)
        abc = a * bc // math.gcd(a, bc)
        l,r = 0,2*10**9    
        
        while l < r:
            mid = (l+r)//2
            if get_num(mid) >= n:
                r = mid
            else:
                l = mid+1

        return l