##### 비교
> 데이터베이스는 기본 키의 값으로 로우를 구분한다. 반면에 객체는 동일성 비교와 동등성 비교라는 두 가지 비교 방법이 있다.
- 동일성 비교는 == 비교다 객체 인스턴스의 주소 값을 비교한다.
- 동등성 비교는 equals() 메서드를 사용해서 객체 내부의 값을 비교한다.
> 따라서 테이블의 로우를 구분하는 방법과 객체를 구분하는 방법에는 차이가 있다.

##### JPA와 비교
> JPA는 같은 트랜잭션일 때 같은 객체가 조회되는 것을 보장한다. 그러므로 다음 코드에서 member1과 member2는 동일성 비교에 성공한다.
```java
String memberId = "100";
Member member1 = jpa.find(Member.class, memberId);
Member member2 = jpa.find(Member.class, memberId);

member1 == member2; // true
```
