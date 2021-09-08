# Generic
- `<K extends T>` T와 T의 자손 타입만 가능 (K는 들어오는 타입으로 지정 됨)
- `<K super T>`	 T와 T의 부모(조상) 타입만 가능 (K는 들어오는 타입으로 지정 됨)
- `<? extends T>` T와 T의 자손 타입만 가능
- `<? super T>` T와 T의 부모(조상) 타입만 가능
- `<?>` 모든 타입 가능. <? extends Object>랑 같은 의미
---
- `<K extends Number>`
  - Number와 이를 상속하는 Integer, Short, Double, Long 등의
  타입이 지정될 수 있으며, 객체 혹은 메소드를 호출 할 경우 K는
  지정된 타입으로 변환이 된다.
- `<? extends T>`
  - Number와 이를 상속하는 Integer, Short, Double, Long 등의 
  타입이 지정될 수 있으며, 객체 혹은 메소드를 호출 할 경우 K는
  지정된 타입으로 변환이 된다.
---
### 제네릭 이해하기
```java
public class ClassName <E extends Comparable<? super E> { ... }
```
위와 같은 제네릭의 형태가 의미하는 바는?
```java
public class SoltClass <E extends Comparable<E>> { ... }	// Error가능성 있음
public class SoltClass <E extends Comparable<? super E> { ... }	// 안전성이 높음
 
public class Person {...}
 
public class Student extends Person implements Comparable<Person> {
	@Override
	public int compareTo(Person o) { ... };
}
 
public class Main {
	public static void main(String[] args) {
		SoltClass<Student> a = new SoltClass<Student>();
	}
}
```
만약 <E extends Comparable<E>>라면 SoltClass<Student> a 
객체가 타입 파라미터로 Student를 주지만, Comparable에서는 그보다 
상위 타입인 Person으로 비교하기 때문에 Comparable<E>의 E인 Student보다 
상위 타입 객체이기 때문에 제대로 정렬이 안되거나 에러가 날 수 있다.

그렇기 때문에 E 객체의 상위 타입, 즉 <? super E> 을 해줌으로써 위와같은 불상사를 방지할 수가 있는 것이다.