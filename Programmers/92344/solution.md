# First Trial
Brute Force로 각각의 cell 하나하나에 대해 연산을 할 경우 시간복잡도가 엄청나게 커지기 때문에 다른 방법을 생각해야 한다.

## 1D Problem

먼저 2차원이 아닌 1차원 문제로 생각하여 접근해보자. 차원이 1이므로, `skill`을 `[c1,c2,degree]`로 정의할 수 있다.

`arr[i]` 를 `board`의 0~i 의 원소에 `arr[i]` 값을 더하는 행위로 생각해 보면 (부분합),
맨 처음에 arr는 아무 연산이 없는 형태로 `[0, ... 0]` 과 같이 정의되고,

`[c1,c2,degree]` 연산은 `arr[c2]` 에 degree를 더하고, `arr[c1-1]`에 degree를 빼주는 연산으로 대체할 수 있다.

(예를 들어, `[3,6,4]`는 0,1,2,3,4,5,6 원소에 4가 더해지고 (`arr[6]`: -4), 0,1,2 원소에는 영향이 없어야 하므로 `arr[2]`는 -4가 된다)

그리고 여러 번의 연산 후 `board[k]` 는 `arr[k] + arr[k+1] + ... + arr[-1]` 연산을 통해 구할 수 있게 되고,

index를 역순으로 계산하면 `board[k] = board[k+1] + arr[k]`로 O(1) 만에 계산할 수 있으므로 board의 크기를 N, 연산의 크기를 M이라고 했을 떄

시간복잡도가 `O(M)`이 된다.

## 2D Problem

이 알고리즘을 2차원에 적용하게 되면, `arr`는 아래와 같이 row와 column 각각에 대해 위와 마찬가지로 c2는 더하고 c1-1는 빼고, r2는 더하고 r1-1는 빼는 방식으로 구할 수 있다. 

다만, 이렇게 되면 범위에 들어가지 않는 `sum_arr[r1-1][c1-1]`가 두번 빼는 연산을 하기 때문에 마지막으로 더해준다.
```python
for type,r1,c1,r2,c2,degree in skill:
    if type == 1:
        degree *= -1
    sum_arr[r2][c2] += degree
    if c1 > 0: sum_arr[r2][c1-1] -= degree
    if r1 > 0: sum_arr[r1-1][c2] -= degree
    if c1 > 0 and r1 > 0: sum_arr[r1-1][c1-1] += degree
```

`sum_arr`를 구하는 데 O(K) (`skill`의 길이는 K라고 하자),

위와 마찬가지로 정답도 역순으로 계산하면 board 크기만큼 걸리므로 O(MN).

따라서 시간복잡도는 O(K+MN) 이 된다.