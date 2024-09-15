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
        heap = []
        for key,value in num_dict.items():
            heap.append((-value,key))

        heapq.heapify(heap)
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
            
        return ans