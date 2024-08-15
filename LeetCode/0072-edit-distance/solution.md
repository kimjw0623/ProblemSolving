# First Trial
word1, word2의 최대 길이가 각각 500이고, 매번 선택할 수 있는 가짓수가 3개이므로 순회하는 것은 불가능

그리고, 알고리즘적으로도 접근하기 힘들었음

따라서 2-dimentional DP를 선택하고 각각의 슬롯이 `word1[:i], word2[:j]` 에서의 solution이 되도록 구성

업데이트 방식은, 채워야 할 슬롯에서 `word1[i] == word2[j]` 이라면 edit distance 가 `dp[i-1][j-1]`와 동일하므로 그대로 채우고,

아니라면 `dp[i-1][j-1],dp[i-1][j],dp[i][j-1]` 중 가장 edit distance 가 작은 것에 +1 을 (각각 replace, addition, addition operation) 하여 채운다.

리트코드 1143. Longest Common Subsequence 와 비슷한 방식!

Time complexity는 O(mn) 이 된다.

# Second Trial
첫 번째 방식은 Space complexity가 O(mn) 인데, cell 업데이트 시 예전의 값을 참고하지 않기 때문에,

업데이트에 필요한 `dp[i-1][j-1],dp[i-1][j]`, `dp[i][j-1]` 를 위해 두 row만 저장하도록 하였음

Space complexity는 O(m) 이 된다. (O(n)으로도 마찬가지로 구현 가능)

# Memo
특정 Data structure, 혹은 graph로 접근하기 힘들다면 1D, 2D DP를 적용해보자
