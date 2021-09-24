# new String() vs "" 의 차이점
![다운로드](https://user-images.githubusercontent.com/67107008/134624565-126fe554-db8e-4d77-b92d-92d905a11f5d.png)

## "" 리터럴 방식
```java
String msg = "hong";
```
위와 같이 문자열을 바로 String에 할당하는 방법을 리터럴 방식이라고 한다.   
위와 같은 방법으로 할당한 문자열은 Java Heap 영역 안에 있는 String Pool에 저장된다. (GC의 대상이 된다.)
String Pool은 똑같은 문자열이 여러번 할당됐을 때 또 다른 메모리 공간을 할당하는게 아니라 변수에 주소값을 동일하게   
할당하는 방법으로 메모리 낭비를 줄인다.

## new String() 방식
```java
String msg = new String("hong");
```
위와 같이 새로운 String 인스턴스를 만드는 방법은 리터럴 방식과 다르게 같은 문자열이라 할지라도   
새로운 인스턴스를 만들고 그 인스턴스는 Java Heap 영역에 생성된다.

## 리터럴 방식은 Immutable(불변)하다.
### Immutable 의 특징
- 장점 : 생성자, 접근메소드에 대한 방어 복사가 필요없다. 
멀티스레드 환경에서 동기화 처리없이 객체를 공유할 수 있다.(Thread-safe)
- 단점 : 객체가 가지는 값마다 새로운 객체가 필요하다. 따라서 메모리 누수와 새로운 
객체를 계속 생성해야하기 때문에 성능저하를 발생시킬 수 있다.
