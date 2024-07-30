# First Trial
옛날에 정답을 보고 푼 문제인데, 다시 풀때 그 해결 방법이 인상깊어 쉽게 풀었음

2차원 DP 문제인데, subproblem array에 무엇을 담을지, 어떻게 subproblem을 이용할 지 잘 생각해야 함

먼저 subproblem array에는 해당 cell을 bottom-right으로 만들 수 있는 가장 큰 정사각형의 변의 길이를 저장

그리고, `sub[i][j]`는 `min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1]) + 1` 로 얻을 수 있는데, 이는 subproblem이 각각 top-right, bottom-left, top-left 까지 얼마나 1로 채워져 있는지 표현하고 있기 때문이다.

아래 그림 참고 [링크](https://leetcode.com/problems/maximal-square/solutions/600149/python-thinking-process-diagrams-dp-approach/?envType=problem-list-v2&envId=oejsgvki):

![image](https://github.com/user-attachments/assets/238e9991-e45d-49cd-a295-b1939c67ef13)


# Memo
다른 문제를 풀 때도 공간복잡도 또한 고려하여 가능하면 제공하는 데이터구조에 덮어 쓸 수 있는지 확인해야 함!
