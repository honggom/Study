# Non-null assertion operator란?
접미에 붙는 느낌표(!) 연산자인 단언 연산자는 해당 피연산자가 null, undeifned가 아니라고 단언해준다.

해당 피연산자가 null, undefined가 아닌 타입의 value를 갖는다고 프로그래머가 단언할 때 에러등을 방지하기 위해 사용한다.

```typescript
// Compiled with --strictNullChecks

function validateEntity(e?: Entity) {

// Throw exception if e is null or invalid entity

}

function processEntity(e?: Entity) {

validateEntity(e);

let s = e!.name; // Assert that e is non-null and access name
```