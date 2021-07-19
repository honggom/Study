## 예외 / Exception
### 체크 예외 (일반 예외)
  : Exception 클래스의 서브 클래스이면서 RuntimeException 클래스를 상속하지 않는다.
- 코드상 예외처리가 되어있지 않으면 컴파일 에러가 발생한다.
    - 고로 명시적인 예외처리가 필요함
    
### 언체크 예외 (실행 예외 / 런타임 예외)
  : Exception 클래스의 서브 클래스이면서 RuntimeException 클래스를 상속한다.
- 실행 중 발생할 수 있는 예외
  - 코드 상 미리 조건을 주의 깊게 체크하면 피할 수 있음 따라서 명시적인 예외처리를 강제하지 않음  
- ex) NullPointerException, ArrayindexOutOfBoundsException 

### 트랜잭션
- 체크 예외 : 체크 예외가 발생해도 트랜잭션은 roll back 되지 않음
- 언체크 예외 : 언체크 예외가 발생하면 트랜잭션은 roll back 됨

### 예외 처리 이유 
- 예외 처리를 하는 주된 목적은 예외가 발생해도 시스템이 계속 동작하기 위함이다.
