## 공통점
1. map 인터페이스를 구현한 클래스
2. key, value 형태의 자료구조

## 차이점
1. HashTable
   - key, value에 null을 허용하지 않음.
   - Hashtable 의 모든 Data 변경 메서드는 syncronized 로 선언되어있다.
   즉, 메서드 호출 전 쓰레드간 동기화 락을 통해 멀티 쓰레드 환경에서 data의 무결성을 보장해준다. `thread-safe`
2. HashMap
   - key, value에 null을 허용한다.
   - `synchrozied`가 선언되어 있지 않음 즉, 멀티 쓰레드 환경에서 `thread-safe` 하지 않다.
3. ConcurrentHashMap
   - key, value에 null을 허용하지 않음.
   - thread-safe 한 HashMap 버전.
   - 동기화를 지원하는 것이 Hashtable과 같지만 성능은 ConcurrentHashMap이 더 우수하다.

## 기타
- 멀티 쓰레드 환경에서의 동기화 락을 통한 동기화 처리는 무조건 필요하지만, 대신 성능이 훨씬 안 좋아진다.
- HashMap은 충돌 문제를 Separate Chaning을 사용하여 처리한다. 또한 worst case 문제는 java8에서 bucket에 적은 data라면 linked list를 사용하지만 많은 data가 쌓이면 Red-Black tree로 변환한다. 따라서 worst case에도 O(logN)의 속도를 보장한다.
