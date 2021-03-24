# day-01 (2021-02-21)
- 상수 선언 === let 상수명: 타입 = 값 
- 변수 선언 === var 변수명: 타입 = 값 
---
### swift 기본(primitive)타입 
 - Bool : true, false
 - Int : 정수
 - UInt : 양의 정수
 - Float : 실수 32비트 
 - Double : 실수 64비트 
 - Chracter
 - String<br>
 기본적으로 swift는 서로 다른 타입과 자료 교환은 암시적으로 불가능 
 ---
 ### Any, AnyObject, nil 
  - Any : 모든 타입을 지칭하는 키워드 
  - AnyObject : 모든 클래스 타입을 지칭하는 프로토콜
  - nil : 없음을 의미하는 키워드 
 ---
 ### Array, Dictionary, Set
  - Array : 순서가 있는 리스트 컬렉션<br>
     > - .append() : 요소 추가 
     > - .contains() : 해당 요소가 있나 확인 true, false 리턴 
     > - .remove(at :0) : 0번째 방의 요소 삭제 
     > - .removeLast() : 마지막 요소 삭제 
     > - .removeAll() : 전체 요소 삭제 
     > - .count() : 개수 확인 
     > - Array[0] : 0번째 변수로 접근 
  - Dictionary : 키와 값의 쌍으로 이루어진 컬렉션 순서가 정해진 것이 아님<br>
     > - anyDic["someKey"] = "someVal" ... 이런식으로 할당 
     > - anyDic.removeValue(forKey: "someKey")  
     > - anyDic["someKey"] = nil ... 위와 같은 표현 
  - Set : 순서가 없고, 멤버가 유일한 컬렉션<br>
     > - someSet.insert(1) : 인서트 방법
     > - someSet.cotains(1) : true
     > - someSet.remove(1) : 지우는 방법
     > - someSet.count : 개수 확인 
     > - let union: Set<Int> = someSet.union(anotherSet) -> 합집합
     > - union.sorted() : 정렬
     > - .intersection() : 교집합
     > - .subtracting() : 차집합
---
# day-02 (2021-02-22)
 - 함수 선언 
   > - 반환값이 있는 경우 : func 함수(매개변수명1: 타입, 매개변수명2: 타입 ...) -> 반환타입 {<br> 함수 구현부 return 반환값}
   > - 반환값이 없는 경우 : 반환타입을 Void로, return 부분 지움 
   > - 가변 매개 변수 : 매개 변수 타입... 으로 작서 가능하며 인자로 여러개가 들어갈 수 있다. 선언시 마지막에 하는게 좋다.
   > - 전달 인자 레이블 : 매개 변수의 가명이라 생각하면 됨 매개변수명 앞에 선언하고 함수 내부 정의 에서는 매개변수명을 사용하고 호출시에는 전달인자 레이블을 사용한다.
   > - var someFunc : (String, Strig) -> Void = greeting(to:from:) >>> 이런식으로 변수에 함수를 할당 가능
 - for in 
   > - ex) var integers = [1,2,3] >>> for integer in integers { code }
   > - ex) Dictionary >>> for(key, value) in someDic{ code } 
 - Optional
   > - 변수 타입에 ! 또는 ? 를 붙여 옵셔널 타입으로 사용 가능 nil이 들어와도 되고 해당 타입 값이 할당돼도 됨 
 - if let 
   > - func printName(name : String) { print(name) } 
   > - var myName: Strig! = nil
   > if let name: String = myName {
   >     printName(name)
   > } else {
   >     print("myName == nil")
   > }
   > ...if let 구절에서 myName이 nil이 아니라면 name에 변수가 할당되기 때문에 변수가 할당되기 때문에 if 문을 탄다.
 - struct (값 타입)
   > - 자바의 클래스라 생각하면 된다.
   > - 생성 후 변수에 할당 후 인스턴스로 사용. 
   > - 함수나 변수에 static 키워드를 선언해주면 따로 변수의 할당 없이 해당 타입으로 바로 사용할 수 있다. 
 - class (참조 타입, 다중 상속 불가능)
   > - 구조체(struct)와 매우 비슷 
   > - 프로퍼티에 static을 선언하면 재정의 불가능
   > - 프로퍼티에 class을 선언하면 재정의 가능
 - enum 
   > - 열거형 자체가 하나의 데이터 타입 열거형의 case 하나 하나가 전부 유의미한 데이터 
 - closure
   > - 함수명이 없는 함수 
 - property
 - property 감시자 
 - 상속 
 - 인스턴스 
 - 옵셔널 체이닝 nil 병합 연산자

