# Generic
어떤 클래스를 모든 타입에 대응하게 미리 만들어놓으면 매우 비효율적이다.   
따라서 타입의 지정은 사용자(개발자)에게 넘기고 구조만 제공하기 위한 방법으로 사용된다.

### Generic 장점
1. 제네릭을 사용하면 잘못된 타입이 들어올 수 있는 것을 컴파일 단계에서 방지할 수 있다.
2. 클래스 외부에서 타입을 지정해주기 때문에 따로 타입을 체크하고 변환해줄 필요가 없다. 즉, 관리하기가 편하다.
3. 비슷한 기능을 지원하는 경우 코드의 재사용성이 높아진다.


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