# First Trial
간단한 binary search 문제

다만 binary search 로 문제를 접근할 때 `left = mid+1`와 `right = mid`을 각각 어느 조건에 넣어야 하는지 잘 생각해야 하는데, 

여기서 먼저 최소의 속도를 구하라고 했으므로 `left = mid+1`를 mid의 속도일 때 `h` 보다 시간이 더 걸릴 때로 놓았음 (mid의 속도일 때 보다 빠른 속도가 정답이므로) 

그리고 마지막으로 `left`가 정답이 되어야 한다.
