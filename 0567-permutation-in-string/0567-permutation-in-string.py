class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False 
        # for loop 돌면서 counter 비교
        str_dict = dict()
        l1 = len(s1)
        for char in s1:
            str_dict[char] = str_dict.get(char,0) + 1
        
        cur_dict = dict()
        for i,char in enumerate(s2):
            if i-l1 < 0:
                str_dict[char] = str_dict.get(char,0) - 1
                if not any(list(str_dict.values())):
                    return True
                continue
            del_char = s2[i-l1]
            str_dict[del_char] = str_dict.get(del_char,0) + 1
            # if del_char in str_dict:
            #     str_dict[del_char] += 1
            # if char in str_dict:
            #     str_dict[char] -= 1
            str_dict[char] = str_dict.get(char,0) - 1
            if not any(list(str_dict.values())):
                return True
                
        return False

