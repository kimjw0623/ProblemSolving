# First Trial
Anagram을 character 를 key로 하고, char의 개수를 value로 하는 dictionary로 정의할 수 있음

따라서 `p`에 대한 Counter 를 정의하고, `s`를 순회하면서 `p`와 같은 length의 substring을 모두 검사하며 만약 두 string의 dictionary가 같다면 정답에 해당 idx를 추가하는 방법

Time complexity는 O(N+M), Space complexity는 O(1)

# Second Trial
sliding window 방식을 사용하여, substring을 left, right으로 정의

dictionary를 First Trial과 같이 정의하고, substring에 char가 추가되었을 때 해당 char의 value에서 1을 빼고, 제외되었을 때는 1을 더하는 방식으로 접근한다. 그러면 모든 key의 value가 모두 0이 될 때 해당 substring이 anagram 이 된다.

해결 방법:

1. right를 `s`의 idx로 순회하면서 `s[idx]` 의 값에서 1을 빼준다. 그 값이 0보다 작다면 substring의 `s[idx]` 개수가 `p` 보다 많다는 뜻이므로 정답이 될 수 없고, 0이 될 때까지 left를 증가시키면서 substring을 줄여나간다.
2. left를 다 증가시켰다면 left, right로 정의된 substring의 길이가 `p`와 같은지 확인하고, 같다면 left를 정답 리스트에 추가 (substring과 `p`의 모든 char의 개수가 같은 상태가 지속되므로, 두 string의 길이만 같다면 필요하지 않은 character가 없음을 보장)

마찬가지로 Time complexity는 O(N+M), Space complexity는 O(1)
