# First Trial
모든 경우를 구하라는 것을 보아 수학적으로 접근하는 것은 아니라고 생각했음

간단히 DFS를 활용하여 valid한 구역인지 판단할 수 있는 N*N 배열과 현재 줄 수, 각 줄의 queen의 index를 저장하는 리스트를 parameter로 가지도록 하였음

첫 번째 줄부터 채워나가며 마지막 줄 까지 채웠다면 각 줄의 queen의 index를 저장하는 리스트를 `ans`에 담는 방식으로 구현

# Memo
- 2차원 배열을 복사할 때 1차원 배열처럼 `b = a[:]` 와 같이 복사하게 되면 내부의 element는 원본과 똑같은 주소를 갖게 된다 (얕은 복사). 
  따라서 `b = [arr[:] for arr in a]` 와 같이 복사해야 한다.