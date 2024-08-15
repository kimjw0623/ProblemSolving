# First Trial
기본 전제는 다음과 같다:
- 특정 element 보다 index 가 크고, 값이 작은 element 들은 계산에서 무시됨. 예를 들어, `[5,4,6,2,3]`에서 4에 대한 계산값은 6이고, 뒤의 값은 고려할 필요 없음

구현:
- 현재 elem보다 값이 작은 element들을 무시하기 위해서 stack 에서 top으로 올라갈수록 아이템들의 값이 작아지는 monotonic stack 을 도입
- 전제를 위해서 `num2`를 역순으로 순회하며 현재 elem 보다 작은 것들은 stack 에서 제외하고 현재 elem을 추가하는 방식으로 stack 관리. 그리고 현재 값보다 큰 elem을 stack 에서 만나면 mapping dictionary에 기록, 없다면 -1 기록

# 메모
- Time complexity는 stack에서 넣고 빼는 전체 연산이 `2*len(nums2)` 를 넘지 않으므로 `O(N+M)`
- 정방향으로 순회하는 로직 구현
