# Webpack
> Webpack은 여러개 파일을 하나의 파일로 합쳐주는 모듈 번들러(Module bundler)이다.

## 1. import / export가 없던 모듈 이전 상황
JavaScript는 script 태그를 사용하여 외부의 스크립트 파일을 가져올 수는 있지만, 
파일마다 독립적인 파일 스코프를 갖지 않고 하나의 전역 객체를 공유한다.  

```html
<!DOCTYPE html>
<html>
  ...
  <body>
    <script src="./src/a.js"></script>
    <script src="./src/b.js"></script>
  </body>
</html>
```
### a.js
```javascript
function mul(x, y) {
  return x * y;
}
```

### b.js
```javascript
mul(3, 4)

console.log(mul(3, 4)); // 12
```
> 문제는 mul이 전역 스코프라는 것이다.
만약 mul에 다른 값을 할당해버리면 mul을 사용하지 못하게 된다.

## 2. IIFE
즉시 실행 함수 표현(IIFE, Immediately Invoked Function Expression)은 정의되자마자 즉시 실행되는 Javascript Function 를 말한다.
```javascript
(function() {
  ...
})()
```

```javascript
(function() {
  const name = "hong"
})()

name // Uncaught ReferenceError: hong is not defined
```
IIFE 내부에서 정의된 변수는 외부 범위에서 접근이 불가능하다.  

IIFE는 스코프 문제를 해결했지만 바로 실행한다는 점에서 모듈화의 해결책은 아니다. 

## 3. CommonJS, AMD
### CommonJS
exports 키워드로 모듈을 만들고 require() 함수로 임포트하는 방식이다.
- 전역변수와 지역변수를 분리하여 모듈이 독립적인 실행 영역을 갖게 된다.
- script 태그로 파일을 가져오는 것이 아니라 필요한 함수나 변수를 가져올 수 있다.
- exports와 require를 이용하여 의존성 관리도 편해졌다.

이렇게 CommonJS는 모듈화의 조건을 충족시키지만 이 방식은 
브라우저에서는 필요한 모듈을 모두 내려받을 때까지 아무것도 할 수 없게 
된다는 결정적인 단점이 있었다.

### AMD
AMD(Asynchronous Module Definition)는 비동기로 로딩되는 환경에서 모듈을 사용하는 
것이 목표다. 이 방식은 define 함수 내에 코드를 작성함으로써 스코프 분리가 가능하다.
```javascript
define(['./a.js', './b.js'], function(a, b){
  ...
})
```
## 4. ES6 Module
ES6에서는 export를 이용해 모듈로 만들고 import로 가져온다.
### a.js
```javascript
function mul(x, y) {
  return x * y;
}
```

### b.js
```javascript
import * as a from "./a.js"

console.log(a.mul(3, 4));
```
import * as name은 모든 export를 가져오고 name은 
모듈 객체의 이름으로, export를 참조 하기위한 네임 스페이스로 사용된다.

ES6에서는 클라이언트 사이드 자바스크립트에서도 동작하는 모듈 기능을 추가했다. 
script 태그에 type="module" 속성을 추가하면 모듈로 사용할 수 있다.

그러나 아직까지는 모든 브라우저에서 지원하지 않기 때문에 브라우저와 무관하게 사용할 수 있는 모듈이 필요하다.

## 4. Webpack
그래서 웹팩을 사용한다. 웹팩은 하나의 시작점(Entry point)으로부터 의존적인 모듈을 전부 찾아내서 하나의 
파일로 만든다.

웹 어플리케이션 개발에 필요한 다양한 요소(HTML, CSS, Javascript, Images, Font, 등...)들을 하나의 
파일로(혹은 여러 개의 파일로) 병합 및 압축을 해주는 역할을 한다. 주요한 요소로는 Entry, Output, 
Loaders, Plugins, Mode, Browser Compatibility가 있다.