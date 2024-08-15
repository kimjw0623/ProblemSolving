# First Trial
`s1`,`s2`,`s3`의 index를 각각 l,r,idx로 정의하고 `s3[idx]`와 `s1[l]`,`s2[r]` 가 각각 일치할 때 `l`,`r`을 각각 1씩 증가시켜 recursive하게 다시 실행하는 방식을 적용하였음

BFS로 구현하였는데 정확성은 통과한듯 했지만 TLE 가 났기 때문에 (Time complexity: `O(2^N)`) 다시 시도

# Second Trial
첫 시도 때 TLE 가 났기 때문에 위의 `l`,`r` pair를 이미 수행했는지를 검사하는 `visited` 를 추가하여 같은 연산을 반복하지 않도록 하였음
Time complexity: `O(N^2)` (visited를 통해서 최대 `len(s1) * len(s2)` 번의 연산을 수행하기 때문)

# Memo
- TLE 가 났을 때 visited / DP 적용하는 방법을 생각해보자
- DFS, DP (space complexity 줄이는 방법까지) 로도 해결해보자
