def solution(ability):
    ans = 0
    
    # dp: key: tuple(or bitmask) of participated student,  value: max score
    dp = {}
    
    def dfs(subject,banned_set):
        nonlocal ans
        if subject >= len(ability[0]):
            return 0
        if tuple(banned_set) in dp:
            return dp[tuple(banned_set)]
        
        max_score = 0
        for ppl_idx in range(len(ability)):
            if ppl_idx in banned_set: continue
            banned_set.add(ppl_idx)
            score = dfs(subject+1,banned_set) + ability[ppl_idx][subject]
            banned_set.remove(ppl_idx)
            max_score = max(max_score,score)
        dp[tuple(banned_set)] = max_score
        
        return max_score
    ans = dfs(0,set())
    
    return ans
