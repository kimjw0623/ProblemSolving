# First Trial
subsequence는 index가 커지는 방향으로 가면서 원하는 원소들만 고르는 방식으로 얻는 list이다.

따라서 두 string의 공통된 subsequence를 구하려면 두 string의 character (`text1[idx1]`, `text2[idx2]`) 쌍을 모두 검사해야 한다.

이를 위해서 2-dimensional array를 만들어 array의 좌표가 각각 `idx1`,`idx2`를 가리키고, 저장하는 값은 가장 긴 subsequence의 길이를 저장하였음

주의할 점은 `text1[idx1] == text2[idx2]` 일 때 `dp[idx1][idx2-1]` 혹은 `dp[idx1-1][idx2-1]`을 사용하지 말고, `dp[idx1-1][idx2-1]`을 활용해야 한다는 것

# Memo
풀이가 생각이 나지 않을 때는 어떻게 subproblem으로 나눌 수 있을지 먼저 생각해 보자
