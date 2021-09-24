# list 와 vector의 차이
- vector는 `thread-safe` 하다.
- list는 `thread-safe` 하지 않다.
  - 따라서 멀티 쓰레드 환경에서 위험하지만, 성능은 좋음.
- 동적으로 배열을 할당할 때 인덱스가 초과되었을 때 
  - vector는 현재 배열의 크기의 100% 증가.
  - list는 현재 배열의 크기의 50% 증가.