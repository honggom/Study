# String vs StringBuffer / StringBuilder
## String
- String은 불변하는 속성을 갖고 있다.
```java
String str = "hello";
str += " world"; 
```
위의 코드는 마치 문자열 hello를 가르키고 있던 str이 world와 더해진 것 처럼 착각할 수 있지만   
"hello world"라는 새로운 문자열을 메모리에 저장하고 str에 새로운 메모리 주소값을 할당하는 행위임   
따라서 초기에 할당했던 "hello"는 GC의 대상이 됨
- String은 위와 같은 특성으로 인해 변하지 않는 문자열을 자주 읽어들이는 경우에 좋은 성능을 기대할 수 있다.
반대로, 문자열 추가, 삭제 등의 연산이 빈번하게 발생하면 힙 메모리에 임시 가비지가 생성되어 힙 메모리
부족으로 인한 성능에 치명적인 영향을 끼치게 된다.

## StringBuffer / StringBuilder
- String의 단점을 보완하기 위해 도입된 클래스들이다.
- 위 두 클래스는 가변성을 가지기 때문에 위에서 예를든 "hello world"가 새로운 인스턴스를 만드는 것이 아닌,
동일 객체내에서 문자열을 변경하는 것이 가능하다.
- 따라서 문자열의 추가 수정, 삭제가 빈번한 경우라면 위 두 클래스를 이용하자.

## StringBuffer vs StringBuilder
- 두 클래스의 차이점은 동기화의 유무이다.
- StringBuffer :
  - StringBuffer는 동기화 키워드를 지원하여 멀티쓰레드 환경에서 안전하다.(thread-safe) 
    - String도 불변성을 가지기 때문에 멀티쓰레드 환경에서 안전하다.
- StringBuilder :
  - StringBuilder는 동기화를 지원하지 않기 때문에 멀티쓰레드 환경에서 사용하는 것은 안전하지 않으나
  동기화를 고려하지 않은 만큼 단일쓰레드 환경에서 StringBuffer보다 성능이 뛰어나다.
