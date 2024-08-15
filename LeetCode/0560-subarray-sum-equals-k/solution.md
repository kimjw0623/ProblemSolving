# First Trial
subarray sum 을 구해야 하기 때문에 `nums`의 첫 번째 원소부터 i번째 원소까지의 합을 저장하는 리스트 `sum_list`를 만듦

그리고 각각의 subarray를 표현하는 left, right index를 만들고 

처음(외부) for loop에서는 해당 리스트의 첫 번째부터 마지막까지 left로 순회하고, 내부의 for loop에서는 left+1 부터 마지막까지 right로 순회하면서

`sum_list[right] - sum_list[left] == k` 를 만족한다면 정답에 1을 더해주는 방법을 사용

하지만 Time complexity가 O(N^2) 이므로 TLE 발생

# Second Trial
정답이 subarray의 개수만을 구하는 것이므로 1st trial에서 내부 loop를 찾는 방식을 순회하면서 찾는 것이 아닌 dictionary로 한번에 접근할 수 있음

dictionary의 key를 subarray sum, value를 첫 번째 원소부터 특정 원소까지의 합이 key인 경우의 수로 지정 (dictionary의 length는 nums.length 보다 작게 됨)

For loop를 nums의 index로 돌면서:
1. 현재 index까지의 합인 `cur_sum`을 관리
2. `sum_dict`에서 `cur_sum - x = k`를 만족하는 x의 개수를 `sum_dict` 에서 구하여 정답에 더하고,
3. `sum_dict`에서  `cur_sum` key의 value 를 1 늘려줌
4. 

따라서 Time complexity는 O(N)

# Memo
정답에서 개수만을 구할 때 dictionary를 사용하여 time complexity를 줄일 수 있음
