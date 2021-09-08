# AOP (Aspect Oriented Programming / 관점 지향 프로그래밍)

- @Pointcut : 어떤 포인트에 적용할 것인지
```java
@Pointcut("execution(* com.example.demo.controller..*.*(..))")
private void cut(){}
```
- @Before (이전) : 어드바이스 타겟 메소드가 호출되기 전에 어드바이스 기능을 수행
```java
@Before("cut()")
public void before(JoinPoint joinPoint){
    MethodSignature ms = (MethodSignature) joinPoint.getSignature();
    Method mt = ms.getMethod();

    System.out.println("method name : "+mt.getName());

     Object[] args = joinPoint.getArgs();

     for(Object obj : args){
         System.out.println("type : "+obj.getClass().getSimpleName());
         System.out.println("value : "+obj);
     }
}
```  
- @After (이후) : 타겟 메소드의 결과에 관계없이(즉 성공, 예외 관계없이) 타겟 메소드가 완료 되면 어드바이스 기능을 수행
- @AfterReturning (정상적 반환 이후) : 타겟 메소드가 성공적으로 결과값을 반환 후에 어드바이스 기능을 수행
```java
@AfterReturning(value = "cut()", returning = "returnObj")
public void afterReturn(JoinPoint joinPoint, Object returnObj){
     System.out.println("return obj");
     System.out.println(returnObj);
}
```  
- @AfterThrowing (예외 발생 이후) : 타겟 메소드가 수행 중 예외를 던지게 되면 어드바이스 기능을 수행
- @Around (메소드 실행 전후) : 어드바이스가 타겟 메소드를 감싸서 타겟 메소드 호출전과 후에 어드바이스 기능을 수행
---
### 적용 내용 : api 요청시 메서드 이름과 리턴값 확인
- 요청 : http://localhost:8080/aop/get/1231231?name=hong
- 컨트롤러 반환 : 1231231 hong
- 콘솔 : 
```
method name : get
type : Long
value : 1231231
type : String
value : hong
get method
get method : 1231231
get method : hong
return obj
1231231 hong
```




- 전체 코드 :
```java
@Aspect
@Component
public class ParameterAop {

   @Pointcut("execution(* com.example.demo.controller..*.*(..))")
   private void cut(){}

   @Before("cut()")
   public void before(JoinPoint joinPoint){
       MethodSignature ms = (MethodSignature) joinPoint.getSignature();
       Method mt = ms.getMethod();

       System.out.println("method name : "+mt.getName());

        Object[] args = joinPoint.getArgs();

        for(Object obj : args){
            System.out.println("type : "+obj.getClass().getSimpleName());
            System.out.println("value : "+obj);
        }
   }

   @AfterReturning(value = "cut()", returning = "returnObj")
   public void afterReturn(JoinPoint joinPoint, Object returnObj){
        System.out.println("return obj");
        System.out.println(returnObj);
   }
}
------------------------------------------------------------------
@RestController
@RequestMapping("/aop")
public class AopController {

    @GetMapping("/get/{id}")
    public String get(@PathVariable Long id, @RequestParam String name){
        System.out.println("get method");
        System.out.println("get method : "+id);
        System.out.println("get method : "+name);
        return id + " " + name;
    }

    @PostMapping("/post")
    public Product post(@RequestBody Product product){
        System.out.println("post method");
        System.out.println("post method : "+product);
        return product;
    }
}
```
---
## 어노테이션으로 AOP 적용하기
- 목적 : 함수의 총 실행시간 구하기
- TimerAop.java : aop 설정
```java
@Aspect
@Component
public class TimerAop {

    @Pointcut("@annotation(com.example.demo.annotation.Timer)")
    private void enableTimer(){}

    @Around("enableTimer()")
    public void around(ProceedingJoinPoint joinPoint) throws Throwable {
        StopWatch sw = new StopWatch();
        sw.start();

        Object result = joinPoint.proceed();
        
        sw.stop();

        System.out.println("total time : "+sw.getTotalTimeSeconds());
    }

}
```
- Timer.java (어노테이션) : 
```java
@Target({ElementType.TYPE, ElementType.METHOD})
@Retention(RetentionPolicy.RUNTIME)
public @interface Timer {
}
```
- AopController.java (컨트롤러) :
```java
@Timer
@DeleteMapping("/delete")
public void delete() throws InterruptedException {
    Thread.sleep(1000 * 2);
}
```
- 요청 : http://localhost:8080/aop/delete / method : delete
- 콘솔 결과 : total time : 2.025214