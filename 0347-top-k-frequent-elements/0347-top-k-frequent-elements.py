class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n)
        # counter를 만들어서 top k 개를 리턴하는 방식은 sorting 이 필요하므로 NlogN
        # k 가 1이면, max 값만 관리
        # k 가 2이면.. 
        ans = []
        num_dict = {}
        for num in nums:
            num_dict[num] = num_dict.get(num,0) + 1
        
        freq_to_value = {}
        for key,value in num_dict.items():
            freq_to_value[value] = freq_to_value.get(value,[]) + [key]
        
        for freq in range(len(nums)+1,0,-1):
            if freq in freq_to_value:
                ans.extend(freq_to_value[freq]) 
        print(freq_to_value)
        return ans[:k]