## 생성자 대신 정적 팩토리 메서드를 고려
> 클래스의 인스턴스를 생성하는 방법은 public 생성자를 이용하는 방법과 정적 팩토리 메서드(static factory method)를 이용하는 방법이 있다.

### public 생성자
```java
public class Book {
    private String name;
    
    public Book(String name) {
        this.name = name;
    }
}
```

### 정적 팩토리 메서드
> 일반적으로 사용하는 생성자로 객체를 생성하는 방법이 아닌 정적(static) 메서드로 하는 방법을 정적 팩토리 메서드라고 한다.

##### public 생성자 대신 제공되는 경우
```java
public class Book {
    private String name;
    
    public static Book withName(String name) {
        Book book = new Book();
        book.name = name;
        return book;
    }
}
```

##### private 생성자와 함께 제공되는 경우
```java
public class Book {
    private String name;
    
    private Book(String name) {
        this.name = name;
    }
    
    public static Book withName(String name) {
        return new Book(name);
    }
}
```

## 정적 팩토리 메서드 장점
##### 1. 이름을 가질 수 있다.
```java
public static void main(String[] args){
    Book book1 = new Book("Effective Java");
    Book book2 = Book.withName("Effective Java");
}
```
> 생성자에 넘기는 매개변수와 생성자 자체만으로는 반환될 객체의 특성을 제대로 설명하지 못한다. 
> > 반면 정적 팩토리 메서드는 이름만 잘 지으면 반환될 객체의 특성을 쉽게 묘사할 수 있다.

```java
public class Book {
    private String name;
    private String author;

    private Book(String name) {
        this.name = name;
    }

    public static Book withName(String name) {
        return new Book(name);
    }

    public static Book withPrice(String author) {
        Book book = new Book();
        book.author = author;
        return book;
    }
}
```

##### 2. 호출될 때마다 인스턴스를 새로 생성하지는 않아도 된다.
- 인스턴스를 미리 만들어 놓거나 새로 생성한 인스턴스를 캐싱하여 재활용하는 식으로 불필요한 객체 생성을 피할 수 있다.
  - 같은 객체가 자주 요청되는 상황에서 성능을 상당히 끌어올려 준다.
- 반복되는 요청에 같은 객체를 반환하는 식으로 정적 팩터리 방식의 클래스는 언제 어느 인스턴스를 살아 있게 할지를 철저히 통제할 수 있다.
  - 인스턴스 통제 클래스라 한다.
    - 싱글턴으로 만들 수 있다.
    - 인스턴스화 불가로 만들 수 있다.
    - 불변 값 클래스에서 동치인 인스턴스가 단 하나뿐임을 보장할 수 있다.

##### 3. 반환 타입의 하위 타입 객체를 반환할 수 있는 능력이 있다.
반환할 객체의 클래스를 자유롭게 선택할 수 있게 하는 엄청난 유연성을 선물한다.
- API를 만들 때 이 유연성을 응용하면 구현 클래스를 공개하지 않고도 그 객체를 반환할 수 있어 API를 작게 유지할 수 있다.
- 프로그래머가 API를 사용하기 위해 익혀야 하는 개념의 수와 난이도가 낮아졌다.
- 프로그래머는 명시한 인터페이스대로 동작하는 객체를 얻을 것임을 알기에 굳이 별도 문서를 찾아가며 실제 구현 클래스가 무엇인지 알아보지 않아도 된다.

##### 4. 입력 매개변수에 따라 매번 다른 클래스의 객체를 반환할 수 있다.
반환 타입의 하위 타입이기만 하면 어떤 클래스의 객체를 반환하든 상관없다.
- 클라이언트는 팩터리가 건네주는 객체가 어느 클래스의 인스턴스인지 알 수도 없고 알 필요도 없다.

##### 5. 정적 팩터리 메서드를 작성하는 시점에는 반환할 객체의 클래스가 존재하지 않아도 된다.
이러한 유연함은 서비스 제공자 프레임워크를 만드는 근간이 된다.