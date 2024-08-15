# First Trial
brute force 로 접근한다면 O(n) 의 시간복잡도를 가질 것이지만, input 들의 범위가 10^9 정도이므로 O(logN) 의 시간복잡도로 생각하였다.
O(logN) 의 시간복잡도를 가지는 알고리즘은 binary search, heap 정도밖에 없으므로 binary search 로 접근하였음

[koko-eating-bananas](https://leetcode.com/problems/koko-eating-bananas/description/) 와 비슷하게 아래 순서로 풀이를 작성하였다.

1. 결과로 가능한 모든 범위를 left, right로 정의
2. 주어진 숫자에 대해서 해당 숫자보다 작은 `ugly number`의 개수를 리턴하는 함수 정의
3. mid의 값이 target `n` 보다 크거나 같을 때 right = mid, 이 외의 경우 left = mid+1 로 binary search 활용

# Memo
binary search를 효율적으로 접근하기 위해 아래 code block과 같은 템플릿을 이용하자.
```python
left, right = a,b # 가능한 값을 모두 포함하도록 left, right 를 정의

while left < right:
  mid = (left+right)//2
  if condition(mid):
    right = mid
  else:
    left = mid+1

return left
```
