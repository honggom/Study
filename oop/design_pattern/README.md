## 전략 패턴
- 필요에 따라 변경이 필요한 알고리즘을 인터페이스를 통해 통째로 외부로 분리시키고,
이를 구현한 구체적인 알고리즘 클래스를 필요에 따라 바꿔 사용할 수 있게 하는 디자인패턴.

## 템플릿 메서드 패턴
- 상속을 통해 슈퍼클래스의 기능을 확장할 때 사용하는 방법
- 변하지 않는 기능은 슈퍼클래스에 만들어두고, 자주 변경되며 확장될 기능은 서브클래스에서 만든다.
- 슈퍼클래스에서는 미리 추상 메서드 또는 오버라이드 가능한 메서드를 정의해두고 이를 활용해 코드의 기본
알고리즘을 담고 있는 템플릿 메서드를 만든다.
- 슈퍼클래스에서 디폴트 기능을 정의해두거나 비워뒀다가 서브클래스에서 선택적으로 오버라이딩할 수 있도록 만들어둔
메서드를 훅 메서드라 한다.
```java
public abstract class Super {
    public void templateMethod() {
        // 기본 알고리즘 ...
        hookMethod();
        abstractMethod();
        ...
    }
    
    protected void hookMethod() {}
    public abstract void abstractMethod(); 
}

public class sub extends Super {
    protected void hookMethod() {
        ...
    }
    
    public void abstractMethod() {
        ...
    }
}
```

## 팩토리 메서드 패턴
- 팩토리 메서드 패턴도 템플릿 메서드 패턴과 마찬가지로 상속을 통해 기능을 확장하게 하는 패턴이다.
- 슈퍼클래스 코드에서는 서브클래스에서 구현할 메서드를 호출해서 필요한 타입의 오브젝트를 가져와 사용한다.
```java 
public abstract class Pizza {
     
    public abstract String getNmae();
 
}

------------------------------------

public class TomatoPizza extends Pizza{
 
    @Override
    public String getNmae() {
        return "TomatoPizza";
    }
 
}

------------------------------------

public class PepperoniPizza extends Pizza{
 
    @Override
    public String getNmae() {
        return "PepperoniPizza";
    }
 
}




------------------------------------

public abstract class Factory {
 
    public abstract Pizza createPizza(String name);
}

------------------------------------

public class PizzaFactory extends Factory{
 
    @Override
    public Pizza createPizza(String name) {
 
        switch (name) {
        case "Tomato": return new TomatoPizza(); 
        case "Pepperoni":return new PepperoniPizza();
        }
         
        return null;
    }
}

------------------------------------

public class Main {
 
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        PizzaFactory pizzaFactory = new PizzaFactory();
        Pizza tomatoPizza = pizzaFactory.createPizza("Tomato");
        Pizza pepperoniPizza = pizzaFactory.createPizza("Pepperoni");
      
    }
}
```

## 템플릿/콜백 패턴 
- 전략패턴의 변환된 형태이며, 반복적인 또는 기본적인 동작들을 템플릿 (아래 코드에서는 myMethod)으로 잡아두고
변화되는 부분을 익명 내부 클래스(람다)로 바로 생성하여 사용하는 패턴이다.
```java
class MyClass {
    void myMethod(PrintB printB) {
        a();

        printB.b();

        c();
    }

    void a() {
        System.out.println("A");
    }

    void c() {
        System.out.println("C");
    }
}

interface PrintB {
    void b();
}

public class Main {
    public static void main(String[] args) {
        MyClass myClass = new MyClass();

        myClass.myMethod(()-> System.out.println("B1"));
        myClass.myMethod(()-> System.out.println("B2"));
    }
}
```