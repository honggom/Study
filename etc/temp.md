# Java
> Java는 `Write Once, Run Anywhere`을 개발 철학으로 두었다. 플랫폼 독립적인 언어를 지향점으로, 같은
> 코드를 어느 운영체제에서나 실행시킬 수 있게 하자는 컨셉을 담고 있다.

Java 프로그래밍 언어로 작성한 소스코드 파일은 단순히 코드만을 담고 있는 파일일 뿐, 이 자체로 무언가가 수행되는 건 아니다. 
따라서 이 파일을 실행하기 위해서는 어떤 과정이 필요하다. 이 과정을 컴파일 이라 하며, 소스 파일은 컴파일을 통해 
.class 확장자를 가진 바이너리 파일로 만들어주어야 한다. 

Java 의 컴파일은 보통 JDK 에 내장되어 있는 javac 컴파일러를 사용하게 된다. 컴파일 후 얻게 된 .class 포맷의 
바이트코드는 수행이 가능한 형태의 파일이다. 그리고 이를 수행하기 위해서는 JRE(Java Runtime Environment) 가 
필요하다. JRE 는 Java 애플리케이션을 실행하기 위한 Java Virtual Machine 을 구현하는 환경인데, JRE 가 드러내는 
특징이 곧 Java 가 모든 권한과 환경에서 실행이 가능하다는 의미이다.

JRE 를 수행하기 위해서는 'java' 라는 프로그램을 호출하여, 컴파일한 바이너리 파일을 인수로 제공하면 된다. 이 때 
java 프로그램은 java 실행환경에 컴파일된 파일을 들고 들어가는 역할을 한다. 즉, java 프로그램은 JVM 을 OS 위에 
하나의 프로세스로 올리는 작업과 함께 바이너리 파일의 로딩도 수행한다. 이렇게 컴파일 타임을 거쳐 생성된 바이너리 파일을 수행하게 
되는 시점이 런타임 이다. 이 시점에는 바이너리 파일을 분석하여 JRE 에 포함된 Java API 와 더불어 Java 프로그램을 수행하게 된다.

- `캡슐화`란 비슷한 역할을 하는 속성과 메소드들을 하나의 클래스로 모은 것을 말한다. 캡슐화에는 정보 은닉 개념이 속해 있는데, 
캡슐 내부의 로직이나 변수들은 감추고 외부에는 api 만을 제공하는 것을 의미한다. 그리고 클래스 내부를 외부에 공개하지 않음으로서 
public 접근 제어자를 가지고 있지 않다면 외부에서 이 클래스의 정보를 마음대로 수정하지 못하게 한다.

- `상속`을 통해서는 특정 클래스의 재사용이 가능하다. 상위 클래스를 하위 클래스에서 상속받게 되면 상위 클래스의 멤버변수나 
메소드를 그대로 물려받을 수 있다. 따라서 코드의 재사용성과 생산성이 증가한다.

- `추상화`란 어떤 실체로부터 공통적인 부분이나 관심있는 특성들을 한 곳에 모은 것을 의미한다. 객체 지향에서 추상화는, 
어떤 하위 클래스들에 존재하는 공통적인 메소드를 인터페이스로 정의하는 것을 예로 들 수 있다.

- `다형성`은 같은 모양의 메소드가 상황에 따라 다르게 동작하는 것을 의미한다. 오버로딩과 오버라이딩이 있는데, 오버로딩이란 
함수 이름은 같지만 파라미터 수, 타입을 다르게 해서 다른 용도로 사용하는 것이다. 오버로딩 개념으로 정의된 경우, 컴파일 시점에 
어떤 메소드가 사용될 지 결정된다. 반면 오버라이딩이란 상위 클래스 메소드를 하위 클래스에서 같은 이름과 형식으로 재정의하는 것을 의미한다. 
오버라이딩 개념으로 정의된 경우, 런타임 시점에 어떤 메소드가 사용될 지 결정된다.

# Spring
1. 클라이언트의 모든 요청을 Dispatcher Servlet이라는 Servlet Class가 받는다. 
2. Dispatcher Servlet(Front Controller)은 요청 URL을 Handler Mapping에게 전달하고, 현재 요청에 알맞는 Controller와 Method에 대한 정보를 알아낸다.
   - 어떤 요청에 어떤 Controller가 동작할지를 xml파일이나 Java파일의 어노테이션으로 설정한다.
   - Spring으로 만들어진 Web Application이 실행될 때, Handler Mapping 객체들이 생성되면서 이런 정보들을 관리한다.
3. Dispatcher Servlet은 HandlerAdapter에게 요청 처리를 위임한다.
4. Handler Adapter는 Controller와 해당 메서드를 실행한다.
   - HandlerMapping은 DispatcherServlet로부터 전달된 URL을 바탕으로 HandlerAdapter 객체를 포함하는 HandlerExecutionChain 객체를 생성하며, 이후 DispatcherServlet이 HandlerExecutionChain 객체로부터 HandlerAdapter 객체를 가져와서 해당 메소드를 실행하게 된다.
5. Controller는 비즈니스 로직을 처리하고, 그 결과를 바탕으로 뷰(ex. JSP)에 전달할 객체를 Model 객체에 저장한다.
   - Dispatcher Servlet에게 View name을 리턴한다.
   - Model : Controller에서 View로 넘겨줄 객체가 저장되는 곳.
6. Dispatcher Servlet은 view name을 View Resolver에게 전달하여 View 객체를 얻는다.
   - 이때 view name뿐만 아니라 accept와 같은 header 정보도 전달된다.
   - header 정보 내의 Accept는 HTML, JSON, XML 일 수 있고, 기본적으로는 HTML이다.
   - View Resolver는 전달된 정보를 바탕으로 사용자에게 보여줄 View가 무엇인지 결정한다.
   - JSP인 경우 JstlView 객체가 생성되며, JstlView 객체가 "xxxx,jsp"에 포워딩하여 결과를 보여준다.(JSP 객체를 생성하는 것이 아니다.)
7. Dispatcher Servlet은 View 객체에 화면 표시를 의뢰한다.
8. View 객체는 해당하는 뷰(ex. JSP, Thymeleaf)를 호출하며, 뷰는 Model 객체에서 화면 표시에 필요한 객체를 가져와 화면 표시를 처리한다.

## DI
## Ioc