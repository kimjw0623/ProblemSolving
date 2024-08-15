# First Trial
input string 의 길이의 범위가 1~16인 것을 보고 dp로 접근

dp[i] 를 `s[:i]` 가 input 일 때의 정답이라고 했을 때, 

s[j:] 가 palindrome 일 경우 dp[j]의 각 가짓수에 `s[j:]` 를 추가한 것들이 정답에 들어가야 할 것이다.

따라서 dp[k]를 구하기 위해서는 j를 0부터 k까지 순회하면서, s[j:k+1] 가 palinedrome일 경우 dp[j]의 각 원소에 s[j:k+1]를 추가하도록 해야 한다.
