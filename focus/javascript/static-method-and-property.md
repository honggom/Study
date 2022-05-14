# 정적 프로퍼티 / 메서드
```javascript
// 생성자 함수
function Person(name) {
  this.name = name;
}

// 정적 프로퍼티
Person.staticProp = 'static prop';

// 정적 메서드
Person.staticMethod = function () {
  console.log('staticMethod');
}

const me = new Person('Lee');

Person.staticMethod() // staticMethod

me.staticMethod() // TypeError : me.staticMethod is not a function
```
> Person 생성자 함수는 객체이므로 자신의 프로퍼티/메서드를 소유할 수 있다. Person 생성자 함수 객체가 소유한 프로퍼티/메서드
> 를 정적 프로퍼티/메서드라고 한다. 정적 프로퍼티/메서드는 생성자 함수가 생성한 인스턴스로 참조/호출할 수 없다.