# `v-if`
조건부로 렌더링하기 위해 `v-if`를 사용한다.
```javascript
<h1 v-if="awesome">Vue is awesome!</h1>
```

# `v-else`
`else`를 적용하기 위해 `v-if`와 함께 사용이 가능하다.
```javascript
<button @click="awesome = !awesome">Toggle</button>

<h1 v-if="awesome">Vue is awesome!</h1>
<h1 v-else>Oh no 😢</h1>
```

# `v-else-if`
```javascript
<div v-if="type === 'A'">
  A
</div>
<div v-else-if="type === 'B'">
  B
</div>
<div v-else-if="type === 'C'">
  C
</div>
<div v-else>
  Not A/B/C
</div>
```

# `v-show`
```javascript
<h1 v-show="ok">Hello!</h1>
```
`v-show`는 항상 렌더링돼서 DOM에 남아있다. 단지 CSS의 display 속성을 토클할 뿐이다.

`v-show`는 `<template>` 엘리먼트는 지원하지 않는다.

# `v-if` vs `v-show`
`v-if`가 토글되는 비용이 더 높고 `v-show`가 초기 렌더링 비용이 더 높다.

토클이 많이 되야하는 상황이면은 `v-show` 그렇지 않으면 `v-if` 사용!

# `v-if` with `v-for`
`v-if`랑 `v-for`를 같이 쓰는 것은 추천되지 않음.

`v-if`랑 `v-for`를 같이 쓰면 `v-if`가 먼저 평가됨. 