class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l,r = 0,0
        idx = 0

        is_valid = []
        visited = set((0,0))
        def recursive(l,r,idx):
            if idx == len(s3):
                if l > len(s1)-1 and r > len(s2)-1:
                    return True
                else:
                    return False
            a,b = False,False
            if l < len(s1) and s1[l] == s3[idx] and (l+1,r) not in visited:
                visited.add((l+1,r))
                a = recursive(l+1,r,idx+1)
            if r < len(s2) and s2[r] == s3[idx] and (l,r+1) not in visited:
                visited.add((l,r+1))
                b = recursive(l,r+1,idx+1)
            return a or b
        return recursive(0,0,0)