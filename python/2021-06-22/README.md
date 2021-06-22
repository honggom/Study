## 데크 (deque)

- 큐를 양방향으로 쓸 수 있게 만든 자료구조
- 양 끝 엘리먼트에 대해서 append와 pop이 가능하다
- 스택과 큐를 동시에 사용이 가능

### 사용법

```python
from collections import deque

deq = deque()

# 데이터가 [1,2,3,4,5,6] 이런식으로 있다고 가정하면 
# 맨 왼쪽 데이터가 1, 맨 오른쪽 데이터가 6  

# 맨 좌측에 데이터를 삽입
deq.appendleft(1)

# 맨 우측에 데이터를 삽입
deq.append(0)

# 맨 좌측에 데이터를 반환 및 삭제
deq.popleft()

# 맨 우측에 데이터를 반환 및 삭제
deq.pop() 
```

### deque의 method
- deque.append(item): item을 데크의 오른쪽 끝에 삽입한다.
- deque.appendleft(item): item을 데크의 왼쪽 끝에 삽입한다.
- deque.pop(): 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
- deque.popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
- deque.extend(array): 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가한다.
- deque.extendleft(array): 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가한다.
- deque.remove(item): item을 데크에서 찾아 삭제한다.
- deque.rotate(num): 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).