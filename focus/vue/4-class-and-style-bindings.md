# Binding to Objects
```javascript
<div :class="{ active: isActive }"></div>
```
객체를 `:class` 를 통해 클래스에게 전달할 수 있다.

위의 구문은 `isActive`값이 `true`이면 `class`어트리뷰트에 `active`어트리뷰트 값이 적용되는 것을 의미한다.

--- 
여러 값을 동시에 적용하는 것도 가능하다.
```javascript
data() {
  return {
    isActive: true,
    hasError: false
  }
}
```
```javascript
<div
  class="static"
  :class="{ active: isActive, 'text-danger': hasError }"
></div>
```
이 템플릿은 아래와 같이 렌더링 된다.
```javascript
<div class="static active"></div>
```
`isActive` 또는 `hasError`값이 바뀌게 되면 클래스 리스트가 업데이트 된다.

예를 들어 `hasError`가 `true`로 값이 바뀌게 되면 클래스 리스트는 `"static active text-danger"`로 변경된다.

--- 
바인딩하는 객체가 꼭 인라인 형태일 필요는 없다.
```javascript
data() {
  return {
    classObject: {
      active: true,
      'text-danger': false
    }
  }
}
```
```javascript
<div :class="classObject"></div>
```
위의 렌더링 결과는 같다.

--- 
computed를 적용하는 것도 가능하다.
```javascript
data() {
  return {
    isActive: true,
    error: null
  }
},
computed: {
  classObject() {
    return {
      active: this.isActive && !this.error,
      'text-danger': this.error && this.error.type === 'fatal'
    }
  }
}
```
```html
<div :class="classObject"></div>
```

---

array를 적용하는 것도 가능하다.
```javascript
data() {
  return {
    activeClass: 'active',
    errorClass: 'text-danger'
  }
}
```
```html
<div :class="[activeClass, errorClass]"></div>
```
위는 아래와 같이 렌더링 된다.
```html
<div class="active text-danger"></div>
```

---
조건부로 클래스 리스트를 적용하는 방법
```html
<div :class="[isActive ? activeClass : '', errorClass]"></div>
```
```html
<div :class="[{ active: isActive }, errorClass]"></div>
```