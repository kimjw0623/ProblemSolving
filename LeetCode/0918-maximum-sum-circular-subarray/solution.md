# First Trial
Circular list 문제의 경우에는 보통 circular 을 활용했을 때와 활용하지 않았을 때를 나눠서 풀게 된다.

이 문제 또한 비슷한데, 

- circular를 활용하지 않았을 때의 max 값은 단순한 maximum subarray 알고리즘(DP)로 구하고
- circular를 사용하지 않은 minimum subarray의 여집합이 circular를 사용한 maximum subarray라는 것을 활용하여 전체 sum 에서 minimum을 빼서 또 다른 값을 구할 수 있다.

이 두 값 중 최댓값을 리턴하도록 하여 풀었다.

# Memo
Kadane's algorithm을 활용하면 공간복잡도 또한 줄일 수 있다: i-1의 dp 값과 현재까지의 max 값, 이 두 변수만을 활용하면 됨
